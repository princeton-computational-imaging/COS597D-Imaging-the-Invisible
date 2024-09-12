import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pathlib
import seaborn as sns  # Import seaborn for high-quality plots

from create_example_image import create_phase_pattern_with_noise

# Parameters for the phase pattern
image_size: int   = 512   # Size of the image
noise_scale: float = 0.1  # Scale of the noise
# Function to create a bad example plot
def plot_bad_example(image: np.ndarray, folder_path: pathlib.Path) -> None:
    plt.imshow(image, cmap='hsv')
    plt.axis('off')  # Hide the axis
    plt.savefig(folder_path / 'bad_example.png', bbox_inches='tight', pad_inches=0)
    plt.close()  # Close the plot to free up memory

# Function to create a better example plot
def plot_better_example(image: np.ndarray, folder_path: pathlib.Path) -> None:
    plt.imshow(image, cmap='gray')
    plt.title('This is a Title', fontsize=8)  # Small and simple title
    plt.colorbar(fraction=0.046, pad=0.04)    # Colorbar with small size
    plt.savefig(folder_path / 'better_example.png', bbox_inches='tight')
    plt.close()  # Close the plot to free up memory


def plot_best_example(image: np.ndarray, folder_path: pathlib.Path) -> None:
    """
    Generates a plot of an image array with physical coordinates normalized to a specified range
    and saves it as a PDF.

    Parameters:
    image (np.ndarray): The image data to plot.
    folder_path (pathlib.Path): The directory path where the plot will be saved.

    Returns:
    None
    """
    sns.set(style='whitegrid')  # Set the seaborn style to whitegrid for a cleaner look

    # Set the figure size for PDF output
    fig, ax = plt.subplots(figsize=(8, 6))  # Width, height in inches
    
    # Plot the image with physical coordinates from -5mm to 5mm for both axes
    cax = ax.imshow(image, cmap='gray', extent=(-5, 5, -5, 5))
    
    # Title and labels with adjusted font sizes
    ax.set_title('Scientifically-Accurate Title', fontsize=24)
    ax.set_xlabel('X-axis label (mm)', fontsize=20)
    ax.set_ylabel('Y-axis label (mm)', fontsize=20)
    
    # Tick parameters for both axes
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    # Aspect ratio set to equal to maintain spatial relations
    ax.set_aspect('equal')
    
    # Adding the colorbar with adjusted size and padding
    fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
    
    # Set tight layout to ensure everything fits without overlapping
    plt.tight_layout()
    
    # Save the plot as a PDF to the specified folder
    plt.savefig(folder_path / 'best_example.png', bbox_inches='tight')
    plt.savefig(folder_path / 'best_example.pdf', bbox_inches='tight')
    plt.close(fig)  # Close the figure to free up memory
    
    
# Create the phase pattern with noise
image: np.ndarray = create_phase_pattern_with_noise(image_size, noise_scale)

# Define the folder path to save the images
folder_path: pathlib.Path = pathlib.Path(r"example_nice_plot")

# Call the functions to generate the plots
plot_bad_example(image, folder_path)
plot_better_example(image, folder_path)
plot_best_example(image, folder_path)
