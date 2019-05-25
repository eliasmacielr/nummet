from itertools import chain
import os

import imageio as imio
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

PCA_FACES_DIR          = 'PCA_faces/'
RECOGNITION_FACES_DIR  = 'recognition_faces/'
IMG_DIM                = 240*240
IMG_DIM_TUPLE          = (240,240)
N_IMAGES               = 150


def main():
    # For each image in PCA_FACES_DIR append it as a column
    faces = np.empty(shape=(IMG_DIM,N_IMAGES), dtype=np.float64)
    pca_faces_imnames = sorted(os.listdir(PCA_FACES_DIR))
    i = 0
    for imname in pca_faces_imnames:
        faces[:,i] = imname2array(PCA_FACES_DIR+imname)
        i += 1
    # Copy faces matrix for projections
    proj_faces = np.matrix.copy(faces)
    # Subtract mean
    mean_face = np.reshape(np.mean(faces, axis=1, dtype=np.float64), (IMG_DIM,1))
    faces -= mean_face

    U, Sigma, Vt = linalg.svd(faces, full_matrices=False)

    # Eigenfaces
    faces = np.matmul(faces, Vt.T[:,:10])

    # Matrix of projected faces of PCA_faces
    for k in range(0, proj_faces.shape[1]):
        v_k = proj_faces[:,k]
        for i in range(0, len(v_k)):
            v_k[i] -= mean_face[i]
        x_hat = np.linalg.lstsq(faces, v_k)[0]
        v_k = np.matmul(faces, x_hat)
        proj_faces[:,k] = v_k

    # Given a face in recognition_faces...
    print('recognition-'+str(faces.shape[1])+'pcs')
    #recognition_faces_imnames = sorted(os.listdir(RECOGNITION_FACES_DIR))
    recognition_faces_imnames = ['my-face.png']
    for imname in recognition_faces_imnames:
        v_face = imname2array(imname)
        for i in range(0, len(v_face)):
            v_face[i] -= mean_face[i]
        x_hat = np.linalg.lstsq(faces, v_face)[0]
        v_face = np.matmul(faces, x_hat)
        # Find min|v_face - v_k|
        min_norm = np.linalg.norm(v_face - proj_faces[:,0])
        k = 0
        for i in range(1, proj_faces.shape[1]):
            norm_k = np.linalg.norm(v_face - proj_faces[:,i])
            if norm_k < min_norm:
                min_norm = norm_k
                k = i
        print(imname + ' -> ' + pca_faces_imnames[k])


def imname2array(imname):
    # Get a list of lists from the image
    imlists = (imio.imread(imname)).tolist()
    # Concat the list of lists to form a np.array
    return np.array(list(chain.from_iterable(imlists)), dtype=np.float64)


if __name__ == '__main__':
    main()
