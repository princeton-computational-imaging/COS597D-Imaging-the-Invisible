import numpy as np
import matplotlib.pyplot as plt
import pathlib

def create_phase_pattern_with_noise(image_size: int, noise_scale: float) -> np.ndarray:
    """
    Create an image similar to the provided sample which is a phase pattern with 
    a quadratic phase and some noise added on top.

    Parameters:
    - image_size: The size of the image (it will be a square image).
    - noise_scale: The standard deviation of the Gaussian noise added to the image.

    Returns:
    - A numpy array representing the generated image with a phase pattern and noise.
    """
    # Create a two-dimensional grid of coordinates
    x = np.linspace(-1, 1, image_size)
    y = np.linspace(-1, 1, image_size)
    
    xx, yy = np.meshgrid(x, y)
    
    # Create the phase pattern
    phase = 10*np.pi * (xx**2 + yy**2)
    
    # Add noise to the phase pattern
    noise = np.random.normal(0, noise_scale, (image_size, image_size))
    noisy_phase = phase + noise
    
    # Normalize the phase to be between -pi and pi
    noisy_phase = (noisy_phase + np.pi) % (2 * np.pi) - np.pi
    
    return noisy_phase

