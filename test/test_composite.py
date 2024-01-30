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

rand_image_data = np.random.rand(10,10)
img_A = Image(rand_image_data)
rand_image_data2 = np.random.rand(10,10)
img_B = Image(rand_image_data2)
rand_image_data3 = np.random.rand(10,10)
img_C = Image(rand_image_data3)


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

def test_reset(): 
    comp_img = Composite(img_A,img_B,img_C)
    comp_img.red.rescale_log()
    comp_img.blue.rescale_log()
    comp_img.green.rescale_log()
    comp_img.reset()
    assert(np.all(rand_image_data == comp_img.red.rescaled_data))
    assert(np.all(rand_image_data2 == comp_img.green.rescaled_data))
    assert(np.all(rand_image_data3 == comp_img.blue.rescaled_data))
    
    
def test_normalize():
    comp_img = Composite(img_A,img_B,img_C)
    comp_img.normalize()
    assert(comp_img.red.rescaled_data.min()==0)
    assert(comp_img.red.rescaled_data.max()==1)

    assert(comp_img.green.rescaled_data.min()==0)
    assert(comp_img.green.rescaled_data.max()==1)

    assert(comp_img.blue.rescaled_data.min()==0)
    assert(comp_img.blue.rescaled_data.max()==1)
    


def test_rescale_root():
    
    test_image =  np.array([[4,9],[16,25]])
    root_img = np.array([[2,3],[4,5]])
    img1 = Image(test_image)
    img2 = Image(test_image)
    img3 = Image(test_image)
    comp_img = Composite(img1,img2,img3)

    comp_img.rescale_root(2)
    assert(np.all(root_img==comp_img.red.rescaled_data))
    assert(np.all(root_img==comp_img.green.rescaled_data))
    assert(np.all(root_img==comp_img.blue.rescaled_data))

    

test_image_data = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])

def test_rotate_left():
    rotated_img = np.array([[3,6,9],[2,5,8],[1,4,7]])
    test_image1 = Image(test_image_data)
    test_image2 = Image(test_image_data)
    test_image3 = Image(test_image_data)
    comp_img = Composite(test_image1,test_image2,test_image3)
    comp_img.rotate_left()

    assert(np.all(comp_img.red.rescaled_data==rotated_img))
    assert(np.all(comp_img.blue.rescaled_data==rotated_img))
    assert(np.all(comp_img.green.rescaled_data==rotated_img))
    


def test_rotate_right():
    rotated_img = np.array([[7,4,1],[8,5,2],[9,6,3]])
    test_image1 = Image(test_image_data)
    test_image2 = Image(test_image_data)
    test_image3 = Image(test_image_data)
    comp_img = Composite(test_image1,test_image2,test_image3)
    comp_img.rotate_right()

    assert(np.all(comp_img.red.rescaled_data==rotated_img))
    assert(np.all(comp_img.blue.rescaled_data==rotated_img))
    assert(np.all(comp_img.green.rescaled_data==rotated_img))



def test_flip_updown():
    flipped_img = np.array([[7,8,9],[4,5,6],[1,2,3]])
    test_image1 = Image(test_image_data)
    test_image2 = Image(test_image_data)
    test_image3 = Image(test_image_data)
    comp_img = Composite(test_image1,test_image2,test_image3)
    comp_img.flip_updown()
    assert(np.all(comp_img.red.rescaled_data==flipped_img))
    assert(np.all(comp_img.green.rescaled_data==flipped_img))
    assert(np.all(comp_img.blue.rescaled_data==flipped_img))