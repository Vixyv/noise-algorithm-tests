from noise import pnoise2, snoise2
from scipy.signal import welch
from random import random, randint

import matplotlib.pyplot as plt
import numpy as np

def generate_noise(func, resolution, scale):
    rand_x = randint(0, 2^12) + random()
    rand_y = randint(0, 2^12) + random()
    return np.array([[func(rand_x+(x/scale), rand_y+(y/scale)) for x in range(resolution)] for y in range(resolution)])

def main():
    # Parameters
    resolution = 4096
    scale = 10

    # Generate Perlin noise
    perlin_noise = generate_noise(pnoise2, resolution, scale)
    # simplex_noise = generate_noise(snoise2, resolution, scale)

    k = 64
    m = int(np.cbrt(resolution/k))

    periodograms = []

    for x in range(int(np.cbrt(k))):
        for y in range(int(np.cbrt(k))):
            # Gets a slice
            subsection = perlin_noise[m*x+1::m*(x+1), m*y+1::m*(x+1)]
            periodograms.append(compute_periodogram(subsection, m))
    
    average = np.zeros(shape=(1024, 1023))

    for periodogram in periodograms:
        average += periodogram

    average = average/len(periodograms)
    plot_data(average)

def compute_periodogram(noise, m):
    # Compute the 2D FFT of the noise
    fft_result = np.fft.fft2(noise)
    fft_shifted = np.fft.fftshift(fft_result)  # Shift zero frequency components to center
    power_spectrum = np.abs(fft_shifted)**2  # Calculate power spectrum

    return power_spectrum/m

def plot_data(power_spectrum):
    # Plotting
    plt.figure()

    # Power Spectrum
    plt.title("Power Spectrum")
    plt.imshow(power_spectrum * 2, cmap='hot')
    plt.axis('off')

    # plt.tight_layout()
    plt.show()

main()