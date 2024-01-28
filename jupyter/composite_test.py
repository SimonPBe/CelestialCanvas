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




from astropy.io import fits


# Replace 'your_file.fits' with the actual path to your FITS file
fits_file_path1 = '502nmos.fits'
fits_file_path2 = '656nmos.fits'
fits_file_path3 = '673nmos.fits'

# Open the FITS file
with fits.open(fits_file_path1) as hdul:
    # Print header information
    header = hdul[0].header
    

    # Access the data
    data_502 = hdul[0].data
    
with fits.open(fits_file_path2) as hdul:
    # Print header information
    header = hdul[0].header
    

    # Access the data
    data_656 = hdul[0].data

with fits.open(fits_file_path3) as hdul:
    # Print header information
    header = hdul[0].header
    

    # Access the data
    data_673 = hdul[0].data


b = Image(data_502)  
g = Image(data_656)
r = Image(data_673)



#a.plot()

#r.normalize().rotate_transpose().rescale_root(1.2).plot()
#g.plot()
#b.plot()



a = Composite(r.normalize().rotate_transpose().rescale_root(1.2),g.normalize().rotate_transpose().rescale_root(2.3),b.normalize().rotate_transpose().rescale_root(1.1))
a.plot()