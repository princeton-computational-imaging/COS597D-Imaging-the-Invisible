# Include as many packages as you'd like here
import numpy as np
from PIL import Image
import skimage.transform
import cv2
import matplotlib.pyplot as plt

# You might need to create the directory (output)
# and commit the complete folder after completing
# the HW.
savedir = '//output//'

def save_fig_as_png(figtitle):
    '''
    
    Saves the current figure into the output folder specificed by the variable "savedir".
    Note: depending on the OS you might change the backslashes / to \.
   
    The figtitle should not contain the ".png".
    
    This helper function should be easy to use and should help you create/save the figures 
    needed for the report.
    
    Hint: The plt.gcf() might come in handy
    Hint 2: read about this to crop white borders
    https://stackoverflow.com/questions/8218608/scipy-savefig-without-frames-axes-only-content  
    
    Args:
        figtile: filename without the ending ".png"
        
    '''

    raise NotImplementedError


def load_image(path):
    """
    TODO: IMPLEMENT ME
    
    Loads an image specified by path.
    
    Specifications on the image:
        1. Image should be returned with type float32 
        2. Image should be scaled between 0 and 1
        3. If the image has a transprancy channel, the output is a 4-channel array
            a) You can test with the image "dog.png" which has an alpha channel

    Args:
        path: path to the file
    Returns:
        output (np.ndarray): The northwesten image as an RGB image (or RGB alpha if 4 channel image)
    """
    
    raise NotImplementedError

def crop_chicago_from_northwestern(img):
    """
    TODO: IMPLEMENT ME
    
    Crop a region-of-interest (ROI) from the big northwestern image that shows only Chicago
    
    The image size should be (250, 1000) and the the output should be an RGB numpy array
    
    Args:
        input (nd.array): The image of Northwestern and Chicago
    Returns:
        output (np.ndarray): The skyline of chicago with size (250,1000,3)
    """
    
    raise NotImplementedError    
def downsample_by_scale_factor(img,scale_factor):
    """
    TODO: IMPLEMENT ME
    
    Downsample the input image img by a scaling factr
    
    E.g. with scale_factor = 2 and img.shape = (200,400)
    
    you would expect the output to be (100,200)
    
    You can use external packages for downsampling. Just look 
    for the right package

    Args:
        input (nd.array): The image of Northwestern and Chicago
    Returns:
        output (np.ndarray): The third dimension shouldn't change, only the first 2 dimensions.
    """
    
    raise NotImplementedError
    



def convert_rgb2gray(rgb):
    """
    TODO: IMPLEMENT ME
    
    rgb2gray converts RGB values to grayscale values by forming a weighted
    sum of the R, G, and B components:

    0.2989 * R + 0.5870 * G + 0.1140 * B 
    
    
    These values come from the BT.601 standard for use in colour video encoding,
    where they are used to compute luminance from an RGB-signal.
    
    Find more information here:
    https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.601-7-201103-I!!PDF-E.pdf

    Args:
        input (nd.array): 3-dimensional RGB where third dimension is ordered as RGB
    Returns:
        output (np.ndarray): Gray scale image of RGB weighted by weighting function from above
    """
    raise NotImplementedError

def plot_chicago_skyline(img):
    """
    TODO: IMPLEMENT ME
    
    This is a simple exercise to learn how to use subplot.
    
    Goal of is to show a 2x2 subplot that shows the Chicagskyline for 
    4 different downsampling factors: 1,2,4,8
    
    Use plt.subplot to create subfigures
    
    You should give a title of the compelte image (use plt.suptitle)
    and each subfigure should have a corresponding title as well.

    Args:
        input (nd.array): 2-dimensional gray scale image
    Returns:
        
    """
    raise NotImplementedError

def rescale(img,scale):
    """
    TODO: IMPLEMENT ME
    
    Implement a function that scales an image according to the scale factor
    defined by scale
    
    If you're using the rescale function from scikit-learn make sure
    that it is not rescaling the 3rd dimension. 
    
    Look at the output of the image and see if looks like expected,
    if not, come up with a solution that solves this problem.

    """    
    raise NotImplementedError

def pad_image(img,pad_size):
    """
    TODO: IMPLEMENT ME
    
    Takes an image and pads it symmetrically at all borders with
    pad_size as the size of the padding

    Args:
        img (np.ndarray): image to be padded
    Returns:
        output (np.ndarray): padded image
    """    
    raise NotImplementedError

def add_alpha_channel(img):
    """
    TODO: IMPLEMENT ME
    
    Takes an image with 3 channels and adds an alpha channel (4th channel) to it
    Alpha channel should be initialize so that it is NOT transparent
    
    Think about what value this should be!
    
    Args:
        img (np.ndarray): rgb imagew without alpha channel
    Returns:
        output (np.ndarray): rgb+depth image
    """    
    raise NotImplementedError


def overlay_two_images_of_same_size(img1,img2):
    """
    TODO: IMPLEMENT ME

    This is a helper function that can be used to implement
    the function "overlay_two_images"
    
    This function takes 2 image of the same input size
    and adds them together via simple superposition.
    
    WARNING: You have to account for the alpha-channel of img2
    to correct for nice superposition of both images
    
    Hint: https://en.wikipedia.org/wiki/Alpha_compositing
    
    Args:
        img1 (nd.array): The image of the background
        img2 (nd.array): The image to be overlayed (e.g. the dog) that has the shape of img1. Img2 should have an alpha channel that has non-zero entries
        location (nd.array): x,y coordinates of the top-left of the image you want to overlay
    Returns:
        output (np.ndarray): An image of the same size   
    """
    
    raise NotImplementedError
    
def overlay_two_images(img1,img2,location):
    """
    TODO: IMPLEMENT ME

    Overlays a background image (img1) with a forgeground image (img1)
    Location defines the tope-left location where img2 is placed ontop of
    the background image1
    
    NOTE: img2 can be a large image and its boundaries could go over
    the image boundaries of the background img1.
    
    You'll have to crop img2 accordingly to fit into img1 and to avoid
    any numpy errors (out-of-bound errors)
    
    Hint: https://en.wikipedia.org/wiki/Alpha_compositing
    
    Args:
        img1 (nd.array): The image of the background
        img2 (nd.array): The image to be overlayed (e.g. the dog)
        location (nd.array): x,y coordinates of the top-left of the image you want to overlay
    Returns:
        output (np.ndarray): An image of size img1.shape that is overlayed with img2
    """    
    
    raise NotImplementedError