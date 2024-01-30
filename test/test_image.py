import sys
sys.path.append("C:/Users/muzu2/Desktop/OpenSourceS/CelestialCanvas")
from CelestialCanvas.image import Image
import numpy as np


def test_reset():
    random_img_data = np.random.rand(10,10)
    rand_img = Image(random_img_data)
    rand_img.rescaled_data = np.random.rand(10,10)

    rand_img.reset()
    assert np.all(rand_img.rescaled_data == random_img_data)

def test_image_normalize():
    random_img_data = np.random.rand(10,10)
    rand_img = Image(random_img_data)
    norm_data = rand_img.normalize().rescaled_data
    assert norm_data.min()==0
    assert norm_data.max()==1


def test_rescale_root():
    test_image =  np.array([[4,9],[16,25]])
    root_img = np.array([[2,3],[4,5]])
    img = Image(test_image)
    img.rescale_root(2)
    assert(np.all(root_img==img.rescaled_data))

    

test_image = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])

def test_rotate_transpose():
    img = Image(test_image)
    transposed_image = np.array([[1,4,7],[2,5,8],[3,6,9]])
    img.rotate_transpose()
    assert(np.all(img.rescaled_data==transposed_image))


def test_rotate_right():
    #img_data = 
    img = Image(test_image)
    rotated_img = np.array([[7,4,1],[8,5,2],[9,6,3]])
    img.rotate_right()
    assert(np.all(img.rescaled_data==rotated_img))

def test_rotate_left():
    img = Image(test_image)
    rotated_img = np.array([[3,6,9],[2,5,8],[1,4,7]])
    img.rotate_left()
    assert(np.all(img.rescaled_data==rotated_img))

def test_flip_updown():
    img = Image(test_image)
    flipped_img = np.array([[7,8,9],[4,5,6],[1,2,3]])
    img.flip_updown()
    assert(np.all(img.rescaled_data==flipped_img))

def test_flip_leftright():
    img = Image(test_image)
    flipped_img = np.array([[3,2,1],[6,5,4],[9,8,7]])
    img.flip_leftright()
    assert(np.all(img.rescaled_data==flipped_img))

    def test_rescale_log():
        test_img_data = np.array([[0,1,2,3],[5,6,7,8]])
        img = Image(np.exp(test_img_data))
        img.rescale_log()
        assert(np.all(img.rescaled_data==test_img_data))