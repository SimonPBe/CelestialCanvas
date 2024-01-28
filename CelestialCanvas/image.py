import matplotlib.pyplot as plt
import numpy as np
        
class Image:
        
    def __init__(self, data ): # wavelength
        self.data = data
        self.rescaled_data = data
        
        
        
    def reset(self): 
        self.rescaled_data = self.data
        return self
        
        
        
    def normalize(self):
        self.rescaled_data = self.rescaled_data=(self.rescaled_data - self.rescaled_data.min()) / (self.rescaled_data.max() - self.rescaled_data.min())
        return self
        

    
    def rescale_root(self,root):
        self.rescaled_data = self.rescaled_data**(root)
        return self


    def rescale_exp(self,scale=1):
        self.rescaled_data = np.exp(self.rescaled_data*scale)
        return self
        
    
    def rotate_transpose(self):
        self.rescaled_data = self.rescaled_data.transpose()
        return self
        
    
    def flip_updown(self):
        self.rescaled_data = np.flipud(self.rescaled_data)
        return self
        

    def flip_leftright(self):
        self.rescaled_data = np.fliplr(self.rescaled_data)
        return self
        
    
    def plot(self,title=""):
        
        plt.imshow(self.rescaled_data, cmap='gray')
        plt.title(title)  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis

        plt.show()
