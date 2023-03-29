import copy


def remove_red(pixel_data):
    """Sets all red channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[0] = 0
    return new_pixel_data


def remove_green(pixel_data):
    """Sets all green channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[1] = 0
    return new_pixel_data


def remove_blue(pixel_data):
    """Sets all blue channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[2] = 0
    return new_pixel_data
