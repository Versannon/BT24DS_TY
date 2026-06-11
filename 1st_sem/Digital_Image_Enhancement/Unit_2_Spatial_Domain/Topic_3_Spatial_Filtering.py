# Spatial filtering
import numpy as np

img = np.random.randint(50, 150, size=(6, 6), dtype=np.uint8)
img[2, 2] = 255 # Salt noise

def median_filter(image):
    h, w = image.shape
    out = np.zeros_like(image)
    pad = np.pad(image, 1, mode='edge')
    for i in range(h):
        for j in range(w):
            out[i, j] = np.median(pad[i:i+3, j:j+3])
    return out

print("Median Filtered:")
print(median_filter(img))
