import matplotlib.pyplot as plt
import numpy as np

class Composite:

    def __init__(self, red, green, blue): # wavelength
        self.red= red.rescaled_data
        self.blue = blue.rescaled_data
        self.green = green.rescaled_data
        self.comp = np.dstack((self.red,self.green,self.blue))

    def plot(self,title=""):
        plt.imshow(self.comp)
        plt.title(title)  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis

        plt.show()




