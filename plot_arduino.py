import serial
import numpy as np
import matplotlib.pyplot as plt



# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600

GUASSIAN_KERNEL = np.array([1, 1]).astype(np.float64)

DELIMITER = ';'

signal_size = 250
frames = 1

MAX_DIST = 200

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #

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

def g_kernal(size, one_d=False):
    """
    Generate a symmetrical kernal using the elegant self convolution style
    :param size: size of intended kernal
    :return: an array of the kernal, centered
    """
    g = GUASSIAN_KERNEL
    # perform N 1D convolutions of the base kernel with itself and save as
    # vector
    for _ in range(size-2):
        g = np.convolve(GUASSIAN_KERNEL, g)

    if one_d:
        s = np.sum(g)
        return g/s
    # create a N by N grid formed by the calculated vector
    x, y = np.meshgrid(g, g.T)
    g = x * y
    s = np.sum(g)
    return g/s

def blur_fourier(im, kernel):
    """
    Blur an image using a Guassian kernal in the fourier freq field.
    :param im: grayscale image
    :param kernal_size: size of the blur kernal
    :return: A blurred image. No edges.
    """
    # kernal = g_kernal(kernal_size)
    # y_pad = (im.shape[0] - kernal_size)/2
    # x_pad = (im.shape[1] - kernal_size)/2
    #
    # filter = np.pad(kernal, ((math.ceil(y_pad), math.floor(
    #     y_pad)), (math.ceil(x_pad), math.floor(x_pad))),
    #                 mode='constant', constant_values=0)
    #
    # blur = DFT2(im) * DFT2(np.fft.ifftshift(filter))
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

device = HOST2DEV[HOST]

guassian = g_kernal(7, one_d=True)
signal = np.zeros((signal_size, frames))

with serial.Serial(device, DEFAULT_BAUD_RATE) as ser:
    while True:
        signal = np.array([str(ser.readline(), 'utf-8')
                           for _ in range(signal_size * frames)])\
            .astype(np.float64).reshape(frames, signal_size)

        # plt.plot(signal)
        # plt.show()
        # tiles = np.tile(signal, (100, 1))

        fourier = np.fft.fft(signal)

        spec = f_spectrum(fourier, True)

        show_dual_plot(np.tile(signal, (100, 1)), np.tile(spec, (100, 1)))

        # except ValueError:
        #     print("error reading stream")







