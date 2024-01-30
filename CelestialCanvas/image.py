import matplotlib.pyplot as plt
import numpy as np
        
class Image:
    """Image object containing the data of one color.

    Args:
        data (array): array containing data of the image whenit was initialized. Used for reset.
        rescaled_data (array): array containing data of iamge after it was modified.
        
        

    """
        
    def __init__(self, data ): # wavelength
        self.data = data
        self.rescaled_data = data
        
        
        
    def reset(self): 
        """Resets recaled_data to data.

        Returns:
            Image: An Image object were recaled_data was reset to data
        
        """
        self.rescaled_data = self.data
        return self
        
        
        
    def normalize(self):
        """Normalizes the data of the image using the maximum and minimum values

        Returns:
            Image: An Image object that was normalized
        
        """
        self.rescaled_data = self.rescaled_data=(self.rescaled_data - self.rescaled_data.min()) / (self.rescaled_data.max() - self.rescaled_data.min())
        return self
        

    
    def rescale_root(self,root):
        """Rescales the data by taking the power using 1/root

        Args:
            root (float): root used for the rescaling 

        Returns:
            Image: An Image object that was rescaled using the root parameter
        
        """
        self.rescaled_data = self.rescaled_data**(1/root)
        return self
    
    def rescale_log(self):
        """Rescales the data using the logarithm function (using log(1+data))


        Returns:
            Image: An Image object that was rescaled using the root parameter
        
        """
        self.rescaled_data = np.log(1+self.rescaled_data)
        return self
        
    
    def rotate_transpose(self):
        """Rotates the data of the image by transposing it

        Returns:
            Image: An Image object that was rotated by transposing it
        
        """
        self.rescaled_data = self.rescaled_data.transpose()
        return self
        
    def rotate_left(self):
        """Rotates the data of the image 90 degrees to the left

        Returns:
            Image: An Image object that was rotated counterclockwise by 90 degrees
        
        """
        self.rescaled_data = np.rot90(self.rescaled_data)


    def rotate_right(self):
        """Rotates the data of the image 90 degrees to the left

        Returns:
            Image: An Image object that was rotated counterclockwise by 90 degrees
        
        """
        self.rescaled_data = np.rot90(self.rescaled_data,-1)


    def flip_updown(self):
        """Flips the data of the image along the 0 axis (up/down)

        Returns:
            Image: An Image object that was flipped upside
        
        """
        self.rescaled_data = np.flipud(self.rescaled_data)
        return self
        

    def flip_leftright(self):
        """Flips the data of the image along the 1 axis (left/right)

        Returns:
            Image: An Image object that was flipped left to right
        
        """
        self.rescaled_data = np.fliplr(self.rescaled_data)
        return self
        
    
    def plot(self,title=""):
        """Plots the constructed composite image

        Args:
            title (:obj:`str`, optional): String containing the title of the image.
                Defaults to an empty string

        """
        
        plt.imshow(self.rescaled_data, cmap='gray')
        plt.title(title)  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis

        plt.show()