import cv2
import matplotlib.pyplot as plt


def get_image_from_emotion(file, h, w):
    img = cv2.imread(file)
    img = cv2.resize(img, (h, w))
    return img


if __name__ == "__main__":
    img = get_image_from_emotion("Images/angry.png", 10, 10)
    # plt.imshow(get_image_from_emotion("angry", 10, 10))
    # plt.show()
    print(img.shape)
