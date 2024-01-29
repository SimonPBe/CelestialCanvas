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
    random_img_data = np.random.rand(10,10)#random something
    rand_img = Image(random_img_data)
    norm_data = rand_img.normalize().rescaled_data
    assert norm_data.min()==0
    assert norm_data.max()==1



