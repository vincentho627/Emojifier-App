import os

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np

from FaceDetection.config import PATH_TO_IMAGES, DATASET_DIRECTORY

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')


def open_Image(img):
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image


def detect_Faces(img, saveRect=True, saveLabelledImg=False, filename='', plot=False):
    """ Detect faces and stores the coordinates in a csv dataset and can save labelled image """
    image, gray_image = open_Image(img)
    faces = faceCascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    print("Found {0} faces!".format(len(faces)))

    if saveRect:
        data = []

        if not os.path.exists(PATH_TO_IMAGES):
            os.mkdir(PATH_TO_IMAGES)
        if not os.path.exists(DATASET_DIRECTORY):
            os.mkdir(DATASET_DIRECTORY)

        index = 0
        for (x, y, w, h) in faces:
            # cropped image
            face_image = image[y:y + h, x:x + w]
            face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
            face_file_name = "{}/{}.jpg".format("Images", index)

            # save cropped image inside image folder
            cv2.imwrite(face_file_name, face_image)
            index += 1
            data.append([face_file_name, x, y, w, h])

        array = np.asarray(data)
        df = pd.DataFrame(array, columns=["image", "x", "y", "width", "height"])
        df.to_csv("{}/faces.csv".format(DATASET_DIRECTORY))

    if saveLabelledImg:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # saving into a jpg
        filename = PATH_TO_IMAGES + "/" + filename
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(filename, image)

    if plot:
        fig, ax = plt.subplots()

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='g', facecolor='none')
            ax.add_patch(rect)
        plt.imshow(image)
        plt.show()
        plt.close(fig)

    return len(faces)


if __name__ == "__main__":
    detect_Faces("/Users/vho001/Desktop/2.jpg")
