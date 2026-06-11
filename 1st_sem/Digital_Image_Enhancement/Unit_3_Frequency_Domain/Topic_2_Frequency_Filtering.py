# FFT filtering
import numpy as np

img = np.zeros((8, 8))
img[::2, ::2] = 1.0

f_shift = np.fft.fftshift(np.fft.fft2(img))
print("FFT Centered (Magnitude):")
print(np.round(np.abs(f_shift), 2))
