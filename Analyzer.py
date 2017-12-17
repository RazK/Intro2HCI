"""
Analyze given signal using fourier filters
"""
import numpy as np
import matplotlib.pyplot as plt  # import matplotlib library
import math
from scipy.ndimage.filters import convolve as convolve


GUASSIAN_KERNEL = np.array([1, 1]).astype(np.float64).reshape(1, 2)

def amplitude(coefficient):
    """
    Calcute the amplitude of a complex coefficient
    :param coefficient: of fourier freq
    :return: real amplitude
    """
    return np.log(1+np.abs(coefficient))

def f_spectrum(im, shifted = False):
    """
    Visualize a fourier freq table as a grayscale image.
    :param im: fourier freq table
    :param shifted: whether or not to center spectrum
    :return: grayscale visualization of fourier spectrum
    """
    if(shifted):
        im = np.fft.fftshift(im)
    f = np.vectorize(amplitude)
    return f(im)

def g_kernel(size, one_d=False):
    """
    Generate a symmetrical kernal using the elegant self convolution style
    :param size: size of intended kernal
    :return: an array of the kernal, centered
    """
    g = GUASSIAN_KERNEL
    # perform N 1D convolutions of the base kernel with itself and save as
    # vector
    for _ in range(size-2):
        g = convolve(GUASSIAN_KERNEL, g)

    if one_d:
        s = np.sum(g)
        return g/s
    # create a N by N grid formed by the calculated vector
    x, y = np.meshgrid(g, g.T)
    g = x * y
    s = np.sum(g)
    return g/s

def blur(im, filter_vec, brighten=False):
    """
    Blur an image using a filter in both x and y directions.
    :param im: image to blur
    :param filter_vec: convolution kernel
    :param brighten: whether or not to induce a brightening scalar, if image
    was intentionally darkened.
    :return: blurred image
    """

    if brighten:
        kernel = filter_vec * 2
    else:
        kernel = filter_vec

    # perform a convolution
    blur = convolve(im, kernel)

    return blur

def blur_fourier(signal, kernel):
    """
    Blur an image using a Guassian kernal in the fourier freq field.
    :param signal: grayscale image
    :param kernal_size: size of the blur kernal
    :return: A blurred image. No edges.
    """

    x_pad = (signal.shape[0] - kernel.shape[0]) / 2


    filter = np.pad(kernel, ((math.ceil(x_pad), math.floor(x_pad)),
                             (math.ceil(x_pad), math.floor(x_pad))),
                    mode='constant', constant_values=0)
    #
    blur = np.fft.fft(signal) * np.fft.fft(np.fft.ifftshift(kernel))
    # return IDFT2(blur).astype(np.float64)
    pass

def show_dual_plot(im1, im2):
    """
    Show 4 images in 4 way plot
    """
    fig = plt.figure()
    f, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
    ax1.imshow(im1, cmap='gray')
    ax2.imshow(im2, cmap='gray')
    plt.show()

class Analyzer():
    """

    """
    def __init__(self):
        self.kernel = g_kernel(7, one_d=True)


if __name__ == "__main__":
    pass

    # guassian = g_kernel(7, one_d=True)