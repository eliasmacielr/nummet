from itertools import chain
import os

import imageio as imio
import matplotlib.pyplot as plt
import numpy as np

PCA_FACES_DIR          = 'PCA_faces/'
RECOGNITION_FACES_DIR  = 'recognition_faces/'
IMG_DIM                = 240*240
IMG_DIM_TUPLE          = (240,240)


def main():
    faces = np.empty(shape=(IMG_DIM,0))
    # For each image in PCA_FACES_DIR append it as a column
    for imname in sorted(os.listdir(PCA_FACES_DIR)):
        faces = np.c_[faces, imname2array(imname)]
    # Compute the mean face and show it
    plt.imshow(np.reshape(np.mean(faces, axis=1), IMG_DIM_TUPLE),
               cmap=plt.get_cmap('gray'))
    plt.show()


def imname2array(imname):
    # Get a list of lists from the image
    imlists = (imio.imread(PCA_FACES_DIR+imname)).tolist()
    # Concat the list of lists to form a np.array
    return np.array(list(chain.from_iterable(imlists)))


if __name__ == '__main__':
    main()
