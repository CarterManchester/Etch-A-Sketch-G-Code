import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from autocorr import autocorr


def detectEdge(imagePath):
    image = loadImage(imagePath)
    if image is not None:
        gaussianImage = gaussian(image)
        sobelImage = sobel(gaussianImage)
        displayImage(sobelImage)
    else:
        print("Error: Image not loaded.")



def loadImage(imagePath):
    try:
        image = mpimg.imread(imagePath)
        return image
    except Exception as e:
        print("Error occorred while loading image: {e}")
        return None
    
def displayImage(image):
    try:
        plt.figure("Display")
        plt.axis('off')
        plt.imshow(image, cmap='gray')
        plt.show()
    except Exception as e:
        print("Error occurred while displaying image: {e}")
        raise



def gaussian(image):
    sigma = 0.2
    try:
        gImage = scipy.ndimage.gaussian_filter(image, sigma=5)

        return gImage
    
    except Exception as e: 
        print("Error occurred while adding gaussian to image: {e}")

def sobel(image):
    bwImage = 0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2] 
    sobelImage = scipy.ndimage.sobel(bwImage, 1)

    return sobelImage



A = 'Fuige.jpeg'
B = 'Clouds.jpg'
C = 'Vader.jpeg'
D = 'Beemer.jpg'
E = 'Fuige2.jpeg'
F = 'FJ.jpg'


detectEdge(F)



