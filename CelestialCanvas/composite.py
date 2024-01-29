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
        self.red= red.rescaled_data
        self.blue = blue.rescaled_data
        self.green = green.rescaled_data
        self.comp = np.dstack((self.red,self.green,self.blue))

    def plot(self,title=""):
        """Plots the constructed composite image

        Args:
            title (:obj:`str`, optional): String containing the title of the image.
                Defaults to an empty string

        """

        plt.imshow(self.comp)
        plt.title(title)  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis

        plt.show()




