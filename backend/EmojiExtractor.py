__author__ = "Justin Chan"

import imageio
import numpy


class EmojiExtractor:
    """
    This class extracts features from an image into a numpy array, which can be read as data
    """
    def __init__(self, path_prefix: str):
        """
        Precondition: path_prefix must be a valid directory, where path[-1] == "/"
        :param path_prefix: the path_prefix of the images being used
        """
        self.path_prefix = path_prefix

    def extract(self, image_name: str) -> numpy.array:
        """
        :param image_name: the name of the image within the directory assigned at initialization, including extension
        :return: a numpy array of the image
        """
        return imageio.imread(self.path_prefix + image_name)


# General case debugging - remove when complete
if __name__ == "__main__":
    ee = EmojiExtractor("Images/")
    print(ee.extract("img_10.png"))
