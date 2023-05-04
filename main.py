import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from skimage import io


def get_image_pixels(image_url):
    """Returns a nested list of the pixels for the image located at image_url"""
    # Fetch the image
    image = io.imread(image_url)
    # Convert the Blue-Green-Red representation to Red-Green-Blue representation
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Get an array of pixels representing the image
    pixel_data = numpy.asarray(image2).tolist()
    return pixel_data


def render_pixels(pixel_data):
    """Displays the image represented by pixel_data"""
    # Write the pixel_data to a local image file
    cv2.imwrite("rendered.jpg", numpy.array(pixel_data))
    # Display that image file
    image = mpimg.imread("rendered.jpg")
    plt.imshow(image)
    plt.show()


def render_my_pic():
    # Use the functions above to fetch pixel data and render the original data
    url = "mycat.png"
    pixel_data = get_image_pixels(url)
    render_pixels(pixel_data)


if __name__ == "__main__":
    render_my_pic()
