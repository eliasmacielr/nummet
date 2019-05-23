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
    i = 0
    for imname in sorted(os.listdir(PCA_FACES_DIR)):
        faces[:,i] = imname2array(PCA_FACES_DIR+imname)
        i += 1
    # Subtract mean
    mean_face = np.reshape(np.mean(faces, axis=1, dtype=np.float64), (IMG_DIM,1))
    faces -= mean_face
    # Calculate covariance
    s = np.cov(faces.T)
    # Obtain eigenvalue and eigenvector
    eigval, V = linalg.eig(s)
    # Sort eigenvalues in descending order
    eigval = np.flip(eigval)
    V = np.fliplr(V)
    # Final data
    faces = np.matmul(faces, V[:,:5])
    # Show the principal eigenvector
    #plt.imshow(np.reshape(faces[:,0], IMG_DIM_TUPLE),
    #           cmap=plt.get_cmap('gray'))
    #plt.show()
    # Given a face in recognition_faces...
    v_face = imname2array(RECOGNITION_FACES_DIR+'wink-11.png')
    for i in range(0, len(v_face)):
        v_face[i] -= mean_face[i]
    v_face = np.linalg.lstsq(faces, v_face)[0]

    imnames = sorted(os.listdir(PCA_FACES_DIR))
    k = 1
    face_i = imname2array(PCA_FACES_DIR+imnames[0])
    for i in range(0, len(face_i)):
        face_i[i] -= mean_face[i]
    face_i = np.linalg.lstsq(faces, face_i)[0]
    min_norm = np.linalg.norm(v_face - face_i)
    print(min_norm)
    for i in range(1, len(imnames)):
        face_i = imname2array(PCA_FACES_DIR+imnames[i])
        for j in range(0, len(face_i)):
            face_i[j] -= mean_face[j]
        face_i = np.linalg.lstsq(faces, face_i)[0]
        norm_i = np.linalg.norm(v_face - face_i)
        print(norm_i)
        if norm_i < min_norm:
            min_norm = norm_i
            k = i
    print(imnames[k-1])
    #plt.imshow(np.reshape(v_face, IMG_DIM_TUPLE),
    #           cmap=plt.get_cmap('gray'))
    #plt.show()


def imname2array(imname):
    # Get a list of lists from the image
    imlists = (imio.imread(imname)).tolist()
    # Concat the list of lists to form a np.array
    return np.array(list(chain.from_iterable(imlists)), dtype=np.float64)


if __name__ == '__main__':
    main()
