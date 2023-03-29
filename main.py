from image_helpers import get_image_pixels, render_pixels


def render_my_pic():
    # Use the functions above to fetch pixel data and render the original data
    url = "https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/pamelafox.jpg"
    pixel_data = get_image_pixels(url)
    render_pixels(pixel_data)

if __name__ == "__main__":
    render_my_pic()