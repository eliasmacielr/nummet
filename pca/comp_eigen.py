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


def main():
    # For each image in PCA_FACES_DIR append it as a column
    faces = np.empty(shape=(IMG_DIM,0))
    for imname in sorted(os.listdir(PCA_FACES_DIR)):
        faces = np.c_[faces, imname2array(imname)]
    # Subtract mean
    mean_face = np.reshape(np.mean(faces, axis=1), (IMG_DIM,1))
    faces = faces - mean_face
    # Calculate covariance
    s = np.cov(np.matrix.transpose(faces))
    # Obtain eigenvalue and eigenvector
    eigval, V = linalg.eig(s)
    # Sort eigenvalues in descending order
    eigval = np.flip(eigval)
    V = np.fliplr(V)
    final_faces = np.matmul(np.matrix.transpose(V), np.matrix.transpose(faces))
    # Show the principal eigenvector
    plt.imshow(np.reshape(final_faces[1,:], IMG_DIM_TUPLE), cmap=plt.get_cmap('gray'))
    plt.show()


def imname2array(imname):
    # Get a list of lists from the image
    imlists = (imio.imread(PCA_FACES_DIR+imname)).tolist()
    # Concat the list of lists to form a np.array
    return np.array(list(chain.from_iterable(imlists)))


if __name__ == '__main__':
    main()
