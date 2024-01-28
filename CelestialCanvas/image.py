class Image:
    def __init__(self, data ): # wavelength
        self.data = data
        #self.wavelength=wavelength
        self.rescaled_data = data
        
        
    def reset(self): 
        self.rescaled_data = self.data
        return self.data
        
        
    def normalize(self):
        self.rescaled_data=(self.rescaled_data - self.rescaled_data.min()) / (self.rescaled_data.max() - self.rescaled_data.min())
        return self.rescaled_data
    
    def rescale_root(self,root):
        self.rescaled_data = self.rescaled_data**(1/root)
        return self.rescaled_data
    
    def rotate(self):
        #?????????transpose,np.flipud,np.fliplr
    
    def plot(self):
        plt.imshow(self.normalize(), cmap='gray')
        plt.title('FITS Image')  # Set the title of the plot
        plt.xlabel('X-axis')  # Set the label for the x-axis
        plt.ylabel('Y-axis')  # Set the label for the y-axis

        plt.show()