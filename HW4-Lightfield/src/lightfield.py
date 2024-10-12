import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2
import scipy
import scipy.misc
from matplotlib import gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import skimage
import skimage.transform as skimage_transform

import os


def bilinear_interpolate_numpy_matrix(data, x, y):
    """
    
    Performs bilinear interpolation on 2D matrix with dimension
    2 x 2
    The locations where you should interpolate are passed by
    the matrices x and y which are in meshgrid format.
    
    HINT: Do NOT use forloops!
    
    HINT: https://gist.github.com/peteflorence/a1da2c759ca1ac2b74af9a83f69ce20e 
    You can copy this code over in a cell in jupyter and play around with
    it until it works. You might want
    
    HINT: Think about what each step is doing here. You need to understand it. 
    You may have to adjust the code not only concerning the variable names but also the order etc.
    
    
    Args:
        data(ndarray): 2D-Array with dimension 2 x 2
        x(ndarray): Meshgrid for coordinates in x
        y(ndarray): Meshgrid for coordinates in y
    
    """
    raise NotImplementedError

def bilinear_interpolate_numpy_2D_image(data, x, y):
    """
    
    Performs bilinear interpolation on 2D matrix with 
    arbitrary size.
    
    You can start with your implementation from bilinear_interpolate_numpy_matrix    
    and check if it works wells. If not, adapt it
    
    The locations where you should interpolate are passed by
    the matrices x and y which are in meshgrid format.
    
    HINT: Do NOT use forloops!
    
    HINT: Think about what each step is doing here. You need to understand it
    
    HINT: https://gist.github.com/peteflorence/a1da2c759ca1ac2b74af9a83f69ce20e 
    You can copy this code over in a cell in jupyter and play around with
    it until it works.
    
    Args:
        data(ndarray): 2D-Array with dimension NxN
        x(ndarray): Meshgrid for coordinates in x
        y(ndarray): Meshgrid for coordinates in y
    
    """
    raise NotImplementedError
    
    
    
    

    
def bilinear_interpolate_numpy_RGB_image(data, x, y):
    """
    
    Performs bilinear interpolation on an RBG image
    that can have arbitrary dimension (e.g. 300x500x3)
    
    You can start with your implementation from bilinear_interpolate_2D_image   
    and check if it works wells. If not, adapt it.
    
        
    HINT: You don't have to use for-loops to deal with the
    color channels. You can achieve everything using
    the .T operator smartly which will do array broadcasting for you
    
    HINT: You might want to use transpose in the end
    to get the correct image dimensions order.
    
    Args:
        data(ndarray): RGB image with arbitrary dimensions
        x(ndarray): Meshgrid for coordinates in x
        y(ndarray): Meshgrid for coordinates in y
    
    """
    raise NotImplementedError
    

    
    
def bilinear_interpolate_numpy(data, x, y):
    """
    
    Performs bilinear interpolation on an RGB-lightfield
        
    You can start with your implementation from bilinear_interpolate_RGB Image 
    and check if it works wells. If not, adapt it.
    
        
    HINT: You don't have to use for-loops to deal with the
    color channels. You can achieve everything using
    the .T operator smartly which will do array broadcasting for you
    
    HINT: You might want to use transpose in the end
    to get the correct image dimensions order.
    
    Args:
        data(ndarray): RGB-lightfield with shape (17, 17, N, M, 3)
        x(ndarray): Meshgrid for coordinates in x
        y(ndarray): Meshgrid for coordinates in y
    
    """
    raise NotImplementedError

    

def get_shift_1D(img,alpha):
    """
    
    Calculates the shifts for each light-field position
    
    Formula given by: $$ (1 - \alpha)\cdot u_k $$
    
    Where u_k is the light-field coordinate ranging from
    -img.shape[0]/2.0 up to img.shape[0]/2.0
    
    Args:
        img(ndarray): 2D-lightfield image with shape (17x300)
        alpha(float): refocus parameter
        
    Returns: 
        shifts(ndarray): 1D-array with shape (17x1) with shifts for each view
    
    """
    raise NotImplementedError


def shift_images_1d(img,shifts):
    """
    Use: scipy.ndimage.shift for the 1D-implementation
    
    Hint: Use mode = 'mirror' to deal with boundaries in a smarter way than zero-filling
    
        
    Args:
        img(ndarray): 2D-lightfield image with shape (17x300)
        shift(ndarray): shift array obtained from get_shift_1d
        
    Returns: 
        out(ndarray): shifted lightfield with same shape as img
    
    """
    raise NotImplementedError


def average_1d_signal(img):
    """
    
    Averages the 2D-lightfield along the the lightfield coorinate
        
    Args:
        img(ndarray): 2D-lightfield image with shape (17x300)        
    Returns: 
         refocused(1d-np.array): 1D-array with shape (Num_pixel x1) that is refocused
    
    """
    raise NotImplementedError

def get_alpha_values():
    """
    
    Write done here a list of interesting alpha values
    where you think it's worth to refocus at
    
    Returns:
        out(array or list): A list with interesting alpha values
    
    """
    raise NotImplementedError


def get_shifts(lf_shape,alpha):
    """
    
    Calculates the amount of shift that needs to be done for each image
    in the light-field which depends on the refocus parameter alpha.
    
    The shift should be returned as two meshgrids for x and y direction.
    
    HINT: This is the straightforward extension from your method
    get_shift_1D which you implemented for 1D-refocusing
    
    HINT:You might need to reverse the direction of u or v shift
    You can do this by simply writing like:
    
    v = - v (if v is the linspace that describes your lightfield coordiantes in v-direction)
    
    Args:
        lf_shape(list): The shape of the lightfield (e.g. (17,17))
        alpha*(float): the refocus paramter
    
    
    Returns:
        DX,DY(ndarray): Meshgrid values that contains the amount of shift
            in x and y coordiantes
    
    """
    raise NotImplementedError


def translate_image(img,dx,dy):
    """
    
    Translates an image by a local shift defined
    by dx and dy
    
    HINT: Use openCV function (e.g. warpAffine)
    
    Args:
        img(ndarray): RGB array or 2D array
        dx,dy(float): amount that image needs to translated
    
    """
    raise NotImplementedError


def shift_lightfield(data,DX,DY):
    """
    
    Shifts each image in the light-field according to the 
    shifts that were specified in get_shifts
    
    HINT: Use 2 for-loops to loop through each light-field position
    
    Args:
        DX,DY(meshgrid): the shifts in x and y for each lightfield position
    
    Returns:
        out(ndarray): a lightfield that was shifted. Same shape as data
    
    """
    raise NotImplementedError



def weight_shifted_ligthfield(data,mask = None):
    """
    
    Weights the lightfield according to the mask thart is provided.
    
    Hint 1: 
        Check if mask equals none. If Mask is none return just data
        otherwise perform the weighting.
        
    
    Hint 2:
    1. With array broadcasting this is a one-liner to code
    2. Use the transpose .T function of Ndarrays twice to get correct shape and dimension.
    
    Args:
        data(ndarray): lightfield data (17,17,Nx,Ny,3)
        mask(ndarray): 2D-matrix of the aperture mask function (can be None if no mask provided)
    
    Returns:
        out(ndarray): weighted lightfield with same sahape
    
    """
    raise NotImplementedError



def crop_part(data,A_mask = None):
    """
    Crops part of the image according to the A_mask used.
    The crop should be performed at the CENTER of the lightfield
    
    DO NOT USE NUMPY COPY FUNCTIONS
    
    Use call-by-reference by simply assessing the subindices and return those.
    
    HINT: Calculate what the center of the lightfield should be. Then substract
    the A_mask.shape[0]/2 to get the top-left index where you should start cropping
    
    HINT: If A_mask == None simply return data, since nothing is to be cropped
    
    Args:
        data(ndarray): lightfield data
        A_mask(ndarray): the aperture image (e.g. 17x17 or 5x5)
    Returns:
        out(ndarray): The cropped lightfield. The first 2 dimension should have shape of A_mask
    
    """
    raise NotImplementedError



def average_shifted_lightfield(tmp_lf,A_mask=None):
    """
    
    Average the registered lightfield. The averaging should be done
    for each channel separately. After that your result will be the refocused image.
    
    If no mask is provided (i.e. A_mask == None) you can simply use the mean
    
    However (this is slightly trickier): if a mask is provided the lightfield
    now is already weighted, i.e. the mean of the image would undersoot the
    actual value. 
    
    In order to get a "weighted" mean simply sum up all values and the normalize
    by the sum of all values of A_mask which will return you the weighted mean.
    
    
    HINT: np.mean and np.sum allows you to do this without writing a for-loop 
    for the color channels! Just specify the axis!
    
    HINT: Try to cast your final image into uint8 
    to avoid any problems with plt.matplotlib
    
    You can use something like this:     refocused = refocused.astype(np.uint8)
    (However you here need to make sure that you values are well rescaled between 0 and 255.)
    
    Args:
        tmp_lf(ndarray): The lightfield after it was cropped and weighted
        A_mask(ndarray): The aperture mask (can also be 0)
        
    Returns:
        out(ndarray 0 uint8): an RGB image which should now be refocused
    
    """
    raise NotImplementedError

