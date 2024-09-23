from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import os
from os import path

def nameChange(folder):
    
    for i, filename in enumerate(os.listdir(folder)):
        print(filename)
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, folder + '_img_' + str(i) + ".Raw")
        os.rename(src, dst)

os.chdir("..")
for filename in os.listdir('HW2_Data'):
    print(filename)
    if filename == 'nameChanger.py':
        pass
    else:
        os.chdir("HW2_Data")
        nameChange(filename)
        os.chdir("..")
