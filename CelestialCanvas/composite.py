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
        self.red.rescaled_data,self.green.rescaled_data,self.blue.rescaled_data = pre_norm_vals




