import sys
#sys.path.append("C:/Users/muzu2/Desktop/OpenSourceS/CelestialCanvas")
from CelestialCanvas.image import Image
from CelestialCanvas.composite import Composite
import numpy as np
from unittest.mock import patch

rand_image_data = np.random.rand(10,10)
def test_composite_init():
    img_A = Image(rand_image_data)
    img_B = Image(rand_image_data)
    img_C = Image(rand_image_data)
    comp_img = Composite(img_A,img_B,img_C)

    #test that composite creates a correct composite image
    pass


@patch('matplotlib.pyplot.figure')
def test_plot_doesnt_change_data(mock_show):
    rand_image_data = np.random.rand(10,10)
    img_A = Image(rand_image_data)
    rand_image_data2 = np.random.rand(10,10)
    img_B = Image(rand_image_data2)
    rand_image_data3 = np.random.rand(10,10)
    img_C = Image(rand_image_data3)
    comp_img = Composite(img_A,img_B,img_C)
    comp_img.plot()
    assert(np.all(rand_image_data == comp_img.red.rescaled_data))
    assert(np.all(rand_image_data2 == comp_img.green.rescaled_data))
    assert(np.all(rand_image_data3 == comp_img.blue.rescaled_data))