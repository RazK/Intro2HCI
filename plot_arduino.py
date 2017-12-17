import serial
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.ndimage.filters import convolve as convolve



# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600

GUASSIAN_KERNEL = np.array([1, 1]).astype(np.float64).reshape(1, 2)

DELIMITER = ';'

signal_size = 250
frames = 1

MAX_DIST = 50

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #
device = HOST2DEV[HOST]

# guassian = g_kernel(7, one_d=True)
signal = np.zeros((signal_size, frames))


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

    # perform a convolution in both directions
    blur = convolve(im, kernel)
    # full_blur = convolve(x_blur, kernel.transpose())
    return blur

# def blur_fourier(signal, kernel):
#     """
#     Blur an image using a Guassian kernal in the fourier freq field.
#     :param signal: grayscale image
#     :param kernal_size: size of the blur kernal
#     :return: A blurred image. No edges.
#     """
#
#     x_pad = (signal.shape[0] - kernel.shape[0]) / 2
#
#
#     filter = np.pad(kernel, ((math.ceil(x_pad), math.floor(
#         y_pad)), (math.ceil(x_pad), math.floor(x_pad))),
#                     mode='constant', constant_values=0)
#     #
#     blur = np.fft.fft(signal) * np.fft.fft(np.fft.ifftshift(kernel))
#     # return IDFT2(blur).astype(np.float64)
#     pass

def show_dual_plot(im1, im2):
    """
    Show 4 images in 4 way plot
    """
    fig = plt.figure()
    f, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
    ax1.imshow(im1, cmap='gray')
    ax2.imshow(im2, cmap='gray')
    plt.show()

guassian = g_kernel(7, one_d=True)

with serial.Serial(device, DEFAULT_BAUD_RATE) as ser:
    while True:
        try:
            signal = np.array([str(ser.readline(), 'utf-8')
                               for _ in range(signal_size * frames)])\
                .astype(np.float64).reshape(frames, signal_size)
        except ValueError as e:
            print("error reading stream")
        signal[0, 0] = 0
        signal[0, -1] = MAX_DIST

        # plt.plot(signal)
        # plt.show()
        # tiles = np.tile(signal, (100, 1))
        blurred = blur(signal, guassian)
        fourier = np.fft.fft(blurred)

        spec = f_spectrum(fourier, True)



        show_dual_plot(np.tile(blurred, (100, 1)), np.tile(spec, (100, 1)))

        # except ValueError:
        #     print("error reading stream")







