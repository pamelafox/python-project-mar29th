from image_helpers import get_image_pixels


def test_get_image_pixels():
    pixels = get_image_pixels(
        "https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/pamelafox.jpg"
    )
    assert len(pixels) == 210
    assert len(pixels[0]) == 150
    assert (pixels[0][0]) == [154, 152, 153]
