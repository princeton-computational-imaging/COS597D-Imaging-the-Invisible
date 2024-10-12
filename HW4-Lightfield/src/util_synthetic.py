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

import code as code

import os

import src.synthetic_aperture as synthetic_aperture



savedir = 'output_synthethic'

def save_fig_as_png(figtitle):
    '''
    Saves the current figure into the output folder
    The figtitle should not contain the ".png".
    This helper function shoudl be easy to use and should help you create the figures 
    needed for the report
    
    The directory where images are saved are taken from savedir in "Code.py" 
    and should be included in this function.
    
    Hint: The plt.gcf() might come in handy
    Hint 2: read about this to crop white borders
    https://stackoverflow.com/questions/8218608/scipy-savefig-without-frames-axes-only-content
    
    '''
    fig = plt.gcf()
    path ='.//' + savedir + '//' + figtitle + str('.png')
    print(path)

    fig.savefig(path,bbox_inches='tight', pad_inches=0)

def plot_image_with_crop(img,window,top_left=None,template=None,top_left_template=None):

    width = img.shape[0]
    height = img.shape[1]
    window_size = window.shape[0]   

    if top_left == None:
        focus_center = (width//2, height//2)
        x0 = focus_center[0] - (window_size//2)
        y0 = focus_center[1] - (window_size//2)
        top_left=(x0,y0)
    
    focus_center = (top_left[0] + (window_size//2),top_left[1] + (window_size//2))
    
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1]) 
    ax = plt.subplot(gs[0])

    # Create a Rectangle patch
    rect = patches.Rectangle((top_left[1],top_left[0]),window.shape[0],window.shape[1],linewidth=3,edgecolor='r',facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    if template is not None:
        rect = patches.Rectangle((top_left_template[1],top_left_template[0]),template.shape[0],template.shape[1],linewidth=2,edgecolor='b',facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(rect)
        
    plt.imshow(img)
    
    plt.scatter(focus_center[1],focus_center[0],color='r')


    plt.title("Original")
    
    
    ax = plt.subplot(gs[1])
    plt.imshow(window)
    
    if template is not None:

        width = window.shape[0]
        height = window.shape[1]

        focus_center = (width//2, height//2)
        template_size = template.shape[0]
        a0 =  focus_center[0] - (template_size//2)
        b0 =  focus_center[1] - (template_size//2)
        a1 =  a0 + (template_size)
        b1 =  b0 + (template_size)

        rect = patches.Rectangle((b0,a0),template.shape[0],template.shape[1],linewidth=2,edgecolor='b',facecolor='none')
        ax.add_patch(rect)

    plt.tight_layout()
    plt.title("Search Window")\
    
    
 

def read_video_to_array(data_path):
    """
    Reads images into a 4D Numpy file
    """
    cap = cv2.VideoCapture(data_path)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1

    cap.release()
    
    buf = buf.transpose([1,2,3,0])
    return buf

def visualizePixelShift(imgs,m_plots=4,n_plots=4):
    """
        This function is to visualize pixel shift in Images
        
        Arguments:
        frames_container - This is the 3D array containg all the float32 type grayscale frames.
        frame_count - The number of frames in the video
        
        This function does not return anything, it just plots the input using matplotlib
    """

    idx = 1
    for k in np.linspace(0, imgs.shape[3],m_plots*n_plots,endpoint=False).astype(int):
   
        plt.subplot(m_plots,n_plots,idx)
        idx = idx + 1
        f = imgs[:,:,:,k]
        plt.imshow(f,cmap='Greys_r')
        plt.title("#" + str(k))
        
        

def visualize_correlation_output(imgs,top_left_list,plot_max=False):
    """
        This function is to visualize pixel shift in Images
        
        Arguments:
        frames_container - This is the 3D array containg all the float32 type grayscale frames.
        frame_count - The number of frames in the video
        
        This function does not return anything, it just plots the input using matplotlib
    """
    idx = 1
    
    m_plots = 3
    n_plots = 8
    for k in np.linspace(0, imgs.shape[0],m_plots*n_plots,endpoint=False).astype(int):
   
        plt.subplot(m_plots,n_plots,idx)
        idx = idx + 1
        f = imgs[k]
        plt.imshow(f)
        if plot_max == True:
            plt.scatter(top_left_list[1,k],top_left_list[0,k],color='red')
        plt.title("#" + str(k))

        
    plt.tight_layout()
    
def display_new_image_location(imgs,top_left_list,top_left_search_window,window_size,img_idx = 0,display_full = True):

    full_image_top_left = top_left_search_window + top_left_list[:,img_idx] - window_size//2


    ax = plt.gca()
    if display_full == True:
        plt.imshow(imgs[:,:,:,img_idx])

        # Create a Rectangle patch
        rect = patches.Rectangle([full_image_top_left[1],full_image_top_left[0]],window_size,window_size,linewidth=3,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        plt.title("# " + str(img_idx))
    else:
        x0 = int(full_image_top_left[0])
        x1 = x0 + window_size
        xc = window_size/2
        y0 = int(full_image_top_left[1])
        yc = window_size/2
        y1 = y0 + window_size
        
        #print(x0,x1,y0,y1)
        
        # We convert to pillow because it has a nice function to handle outside values
        im = Image.fromarray(np.uint8(imgs[:,:,:,img_idx]))
        im = im.crop((y0,x0,y1,x1))
        
        plt.imshow(im)
        plt.scatter(xc,yc,color='r')
        plt.title("# " + str(img_idx))
        


    
def display_new_image_location_all(imgs,top_left_list,top_left_search_window,window_size,display_full = True):
    
    idx = 1
    
    m_plots = 3
    n_plots = 4
    
    for k in np.linspace(0, imgs.shape[3],m_plots*n_plots,endpoint=False).astype(int):
   
        plt.subplot(m_plots,n_plots,idx)
        idx = idx + 1
        display_new_image_location(imgs,top_left_list,top_left_search_window,window_size,k,display_full)
    

def show_registered_images(imgs_translated,top_left_search_window,window_size):

    m_plots = 4
    n_plots = 4

    x0 = top_left_search_window[0]
    x1 = x0 + window_size
    y0 = top_left_search_window[1]
    y1 = y0 + window_size
    
    xc = window_size/2
    yc = window_size/2

    idx = 1
    for k in np.linspace(0, imgs_translated.shape[3],m_plots*n_plots,endpoint=False).astype(int):

        plt.subplot(m_plots,n_plots,idx)
        idx = idx + 1
        plt.imshow(imgs_translated[x0:x1,y0:y1,:,k])
        plt.scatter(xc,yc,color='r')
        plt.title("# " + str(k))
        
def calculate_synthethic_aperture_image(imgs,focus_center=(120,210),window_size=180,template_size = 30,method='cv2.TM_CCOEFF_NORMED'):
    """
    
    Args:
    
    Returns:
        windows_size The size of the window. You can vary this if wanted.
    
    """
     # The template size. This parameter might need to be varied to work well

    window, template, top_left_search_window, top_left_template= synthetic_aperture.crop_search_window(imgs,window_size,template_size,focus_center)
    correlated, top_left_correlated_list = synthetic_aperture.findCorrelationAll(window,template,method)
    top_left_correlated = synthetic_aperture.correct_correlation_result_to_image_coordinates(top_left_correlated_list,imgs,window,template)
    pixel_shifts = synthetic_aperture.calculate_pixel_shifts(top_left_correlated)
    imgs_translated = synthetic_aperture.translate_all_images(imgs,pixel_shifts)
    img_synthethic = synthetic_aperture.average_images(imgs_translated)

    return img_synthethic