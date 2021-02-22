import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np


faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')


def open_Image(img):
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image


def detect_Faces(img, saveRect=True, saveImg=False, filename=''):
    """ Detect faces and stores the coordinates in a csv dataset and can save labelled image """
    image, gray_image = open_Image(img)
    faces = faceCascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    print("Found {0} faces!".format(len(faces)))

    fig, ax = plt.subplots()

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='g', facecolor='none')
        ax.add_patch(rect)

    if saveRect:
        data = []
        for (x, y, w, h) in faces:
            data.append([x, y, w, h])

        array = np.asarray(data)
        df = pd.DataFrame(array, columns=["x", "y", "width", "height"])
        df["name"] = np.nan
        df.to_csv("dataset/faces.csv")

    if saveImg:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # saving into a jpg
        filename = "images/" + filename
        cv2.imwrite(filename, image)

    plt.imshow(image)
    plt.show()