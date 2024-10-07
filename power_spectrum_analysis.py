from noise import pnoise2, snoise2
from random import random, randint

import matplotlib.pyplot as plt
import numpy as np

def generate_noise(noise_func, resolution, scale):
    rand_x = randint(0, 2^12)
    rand_y = randint(0, 2^12)
    return np.array([[noise_func(rand_x+(x/scale), rand_y+(y/scale)) for x in range(resolution)] for y in range(resolution)])

# Computes Bartlett's power spectrum estimation for a 2D signal (assumes the 2D signal is a square)
def bartlett_2d(signal, k):
    periodograms = []

    k_1d = int(np.sqrt(k)) # Makes k (the number of subsections) 1D
    m = int(len(signal)/k) # Length of each subsection of the signal

    # Divides the signal into subsections and computes a peridogram for each subsection
    for y in range(k_1d):
        for x in range(k_1d):
            subsection = slice_2d(signal, (m*x, m*(x+1)-1),  (m*y, m*(y+1)-1))
            periodograms.append(compute_periodogram(subsection))
    
    # Averages peridograms
    power_spectrum = np.zeros((m, m))

    for pdg in periodograms:
        power_spectrum += pdg
    
    return power_spectrum / k

# Returns a subslice of a 2D list (inclusive of start and end indices)
def slice_2d(matrix, x_slice: tuple[int, int], y_slice: tuple[int, int]):
    x_start, x_end = x_slice
    y_start, y_end = y_slice

    list_slice = []

    for y in range(y_end - y_start + 1):
        list_slice.append([])
        for x in range(x_end - x_start + 1):
            list_slice[y].append(matrix[y + y_start][x + x_start])
    
    return list_slice
            
def compute_periodogram(noise):
    # Compute the 2D FFT of the noise
    fft_result = np.fft.fft2(noise)
    fft_shifted = np.fft.fftshift(fft_result)  # Shift zero frequency components to center
    power_spectrum = np.abs(fft_shifted)**2  # Calculate power spectrum

    return normalize_2d(power_spectrum)

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix / norm 
    return matrix

def plot_data(power_spectrum):
    plt.figure()

    plt.imshow(power_spectrum, cmap='gray')
    plt.axis('off')

    plt.title("Power Spectrum")
    plt.savefig("power_spectrum.svg")
    plt.show()



if __name__ == '__main__':
    # simplex_noise = generate_noise(snoise2, resolution, scale)

    perlin_noise = generate_noise(pnoise2, 20000, 2)
    plot_data(bartlett_2d(perlin_noise, 500))