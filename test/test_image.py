
from CelestialCanvas.image import Image
import numpy as np

def test_image_normalize():
    random_img_data = np.random.rand(10,10)#random something
    rand_img = Image(random_img_data)
    norm_data = rand_img.normalize().rescaled_data
    assert norm_data.min()==0
    assert norm_data.max()==1