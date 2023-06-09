from image_filters import remove_blue, remove_green, remove_red


def test_remove_red():
    assert remove_red([[[0, 0, 0], [255, 0, 0]], [[0, 255, 0], [0, 0, 255]]]) == [
        [[0, 0, 0], [0, 0, 0]],
        [[0, 255, 0], [0, 0, 255]],
    ]
    assert remove_red([[[0, 0, 0], [100, 0, 0]], [[150, 255, 0], [255, 0, 255]]]) == [
        [[0, 0, 0], [0, 0, 0]],
        [[0, 255, 0], [0, 0, 255]],
    ]


def test_remove_green():
    assert remove_green([[[0, 0, 0], [255, 0, 0]], [[0, 255, 0], [0, 0, 255]]]) == [
        [[0, 0, 0], [255, 0, 0]],
        [[0, 0, 0], [0, 0, 255]],
    ]
    assert remove_green([[[0, 0, 0], [255, 100, 0]], [[0, 255, 0], [0, 150, 255]]]) == [
        [[0, 0, 0], [255, 0, 0]],
        [[0, 0, 0], [0, 0, 255]],
    ]


def test_remove_blue():
    assert remove_blue([[[0, 0, 0], [255, 0, 0]], [[0, 255, 0], [0, 0, 255]]]) == [
        [[0, 0, 0], [255, 0, 0]],
        [[0, 255, 0], [0, 0, 0]],
    ]
    assert remove_blue([[[0, 0, 0], [255, 0, 100]], [[0, 255, 150], [0, 0, 255]]]) == [
        [[0, 0, 0], [255, 0, 0]],
        [[0, 255, 0], [0, 0, 0]],
    ]
