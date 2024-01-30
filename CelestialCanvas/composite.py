import matplotlib.pyplot as plt
import numpy as np

class Composite:
    """Composite Image created using three Image objects.

    Args:
        red (array): array containing data of the red channel in the image
        green (array): array containing data of the green channel in the image
        blue (array): array containing data of the blue channel in the image
        comp (array): array containing the data of the red, green and blue channels stacked depth wise
        

    """

    def __init__(self, red, green, blue): # wavelength
        self.red= red
        self.blue = blue
        self.green = green
        self.comp = np.dstack((self.red.rescaled_data,self.green.rescaled_data,self.blue.rescaled_data))
        

    def reset(self): 
        """Resets recaled_data for all three images.

        Returns:
            Composite: A Composite object were rescaled_data of all images was reset to data
        
        """
        self.red.reset()
        self.green.reset()
        self.blue.reset()
        return self
        
        
        
    def normalize(self):
        """Normalizes the data of all three images of the composite

        Returns:
            Composite: A Composite object were rescaled_data of all images was normalized
        
        """
        self.red.normalize()
        self.green.normalize()
        self.blue.normalize()
        return self
        

    
    def rescale_root(self,root):
        """Rescales the data of all three images by taking the power using 1/root

        Args:
            root (float): root used for the rescaling 

        Returns:
            Composite: A Composite object were all images were rescaled using the root parameter
        
        """
        self.red.rescale_root(root)
        self.green.rescale_root(root)
        self.blue.rescale_root(root)
        return self
    
    def rescale_log(self):
        """Rescales the data of all three images using the logarithm function

        Returns:
            Composite: A Composite object were all images were rescaled using the logarithm
        """
        self.red.rescale_log()
        self.green.rescale_log()
        self.blue.rescale_log()
        return self
        
    def rescale_custom(self,func):
        """Rescales the data of all three images using a given custom function

        Args:
            func (function): function used for the rescaling 

        Returns:
            Composite: A Composite object were all images were rescaled using the given function

        """
        self.red.rescale_custom(func)
        self.green.rescale_custom(func)
        self.blue.rescale_custom(func)
        return self
    
        
    def rotate_left(self):
        """Rotates the data of the composite image 90 degrees to the left

        Returns:
            Composite: A Composite object that was rotated counterclockwise by 90 degrees
        
        """
        self.red.rotate_left()
        self.green.rotate_left()
        self.blue.rotate_left()
        return self


    def rotate_right(self):
        """Rotates the data of the Composite image 90 degrees to the left

        Returns:
            Composite: A Composite object that was rotated counterclockwise by 90 degrees
        
        """
        self.red.rotate_right()
        self.green.rotate_right()
        self.blue.rotate_right()
        return self


    def flip_updown(self):
        """Flips the data of the Composite image along the 0 axis (up/down)

        Returns:
            Composite: An Composite object that was flipped upside
        
        """
        self.red.flip_updown()
        self.green.flip_updown()
        self.blue.flip_updown()
        return self
        


    def plot(self,title=""):
        """Plots the constructed composite image

        Args:
            title (:obj:`str`, optional): String containing the title of the image.
                Defaults to an empty string

        """
        pre_norm_vals = self.red.rescaled_data,self.green.rescaled_data,self.blue.rescaled_data

        self.comp = np.dstack((self.red.normalize().rescaled_data,self.green.normalize().rescaled_data,self.blue.normalize().rescaled_data))
        
        plt.imshow(self.comp)
        
        plt.title(title)  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis
        plt.show()
        [self.red.rescaled_data,self.green.rescaled_data,self.blue.rescaled_data] = pre_norm_vals




