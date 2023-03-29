import copy

import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from skimage import io

RANDOM_GLOBAL_VARIABLE = 'im so cool'

def sum(a, b):
    return a + b

def get_image_pixels(image_url):
    """Returns a nested list of the pixels for the image located at image_url"""
    # Fetch the image
    image = io.imread(image_url)
    # Convert the Blue-Green-Red representation to Red-Green-Blue representation
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Get an array of pixels representing the image
    pixel_data = numpy.asarray(image2).tolist()
    for row in pixel_data:
        for pixel in row:
            pixel[0], pixel[2] = pixel[2], pixel[0]
    return pixel_data


def render_pixels(pixel_data):
    """Displays the image represented by pixel_data"""
    # Write the pixel_data to a local image file
    transformed_data = copy.deepcopy(pixel_data)
    for row in transformed_data:
        for pixel in row:
            pixel[0], pixel[2] = pixel[2], pixel[0]
    cv2.imwrite("rendered.jpg", numpy.array(transformed_data))
    # Display that image file
    image = mpimg.imread("rendered.jpg")
    plt.imshow(image)
    plt.show()
