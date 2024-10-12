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

import src.lightfield as lightfield

savedir = 'output_lightfield'

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

def load_image(path,scale=1):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #image = cv2.normalize(image.astype('float32'), None, 0.0, 1.0, cv2.NORM_MINMAX) 

    scale_percent = scale # percent of original size
    width = int(image.shape[1] * scale_percent)
    height = int(image.shape[0] * scale_percent)
    dim = (width, height)
    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
    
    return resized

def load_dataset(folder,scale):
    """
    
    Hint: You can use sorted to sort after glob if you use glob
    
    """
    files = sorted(glob.glob(folder + "*"))
      
    tmp = load_image(files[0],scale)
    
    size = int(np.sqrt(len(files)))
    
    img = np.zeros([size,size,tmp.shape[0],tmp.shape[1],tmp.shape[2]],dtype=tmp.dtype)
    
    print(img.shape)
    
    for file in files:
        print(file)
        
        tmp = os.path.basename(file)
        tmp = tmp.split("_")

        u_idx = int(tmp[1])
        v_idx = int(tmp[2])
        
        img[u_idx,v_idx,:,:,:] = load_image(file,scale)
    
    return img


def load_dataset_old(folder,scale):
    """
    
    Hint: You can use sorted to sort after glob if you use glob
    
    """
    files = sorted(glob.glob(folder + "*"))
    
    img = []
    
    for file in files:
        print(file)
        img.append(load_image(file,scale))
    
    img = np.array(img)
    
    return img

def data_reshaper(data,order="C"):
    size = int(np.sqrt(data.shape[0]))
    N_x = data.shape[1]
    N_y = data.shape[2]
    data = np.reshape(data,[size,size,N_x,N_y,3],order)
    return data


def plot_images_grid(imgs,m_plots=3,n_plots=3,x0=None,x1=None,y0=None,y1=None):
    """
    
    Plots the images in a grid.
    
    HINT: Make sure that parameters actually work!
    
    Args:

    """
    
    N_u = imgs.shape[0]
    N_v = imgs.shape[1]
    
    count = 0
    
    u_range = np.linspace(0,N_u-1,m_plots).astype(np.uint16)
    v_range = np.linspace(0,N_v-1,n_plots).astype(np.uint16)


    for u in u_range:
        for v in v_range:
            count += 1
            plt.subplot(m_plots,n_plots,count)
            plt.imshow(imgs[u,v,x0:x1,y0:y1,:].squeeze())
            plt.title(str(u) + " | " + str(v),fontsize=15)
            plt.axis('off')
    
    plt.tight_layout()
    
    

def plot_1D_signal(img,alpha):
    plt.plot(img)
    plt.xlim(0,img.shape[0])
    plt.grid()
    plt.title(r"Refocused with $\alpha$ = " + str(alpha))



def listComplementElements(list1, list2):
    storeResults = []

    for num in list1:
        if num not in list2: # this will essentially iterate your list behind the scenes
            storeResults.append(num)

    return storeResults

def calculate_field_of_depth(img_shifted):

    test = np.abs(np.gradient(img_shifted)[1])
    bla = np.mean(test,axis=0)

    peaks_all, _ = scipy.signal.find_peaks(bla, prominence=10, width=5)
    peaks_width, _ = scipy.signal.find_peaks(bla, prominence=10)
    
    peaks = listComplementElements(peaks_width, peaks_all)
    peaks = np.array(peaks)
    
    return peaks.min(),peaks.max()

def get_disk_aperture(radius):
    """
    Returns a circular aperture. Because of aliasing artefacs we're downsampling the
    HR-image of the circular mask
    
    The mask should be normalized so that it's maximum value is always 1!
    
    """
    A_circle_big = skimage.morphology.disk(128)

    size = radius*2 - 1
    
    out = skimage_transform.resize(A_circle_big.astype(float),[size,size])
    
    out = out/out.max()
    return out


def compute_refocused(data,alpha,A_mask = None):
   
    data_tmp = lightfield.crop_part(data,A_mask)

    DX, DY = lightfield.get_shifts(data_tmp.shape,alpha)

    tmp_lf = lightfield.shift_lightfield(data_tmp,DX,DY)

    tmp_lf = lightfield.weight_shifted_ligthfield(tmp_lf,A_mask)
    
    refocused = lightfield.average_shifted_lightfield(tmp_lf,A_mask)

    return refocused