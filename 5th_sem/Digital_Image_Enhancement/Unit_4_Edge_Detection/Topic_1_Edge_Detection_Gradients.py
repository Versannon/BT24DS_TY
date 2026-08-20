# Edge Detection Sobel Convolution
import numpy as np

img = np.zeros((6, 6))
img[:, 3:] = 10.0 # Vertical edge

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
grad_x = np.zeros_like(img)
for i in range(1, 5):
    for j in range(1, 5):
        grad_x[i, j] = np.sum(img[i-1:i+2, j-1:j+2] * sobel_x)
print("Gradient X:")
print(grad_x)
