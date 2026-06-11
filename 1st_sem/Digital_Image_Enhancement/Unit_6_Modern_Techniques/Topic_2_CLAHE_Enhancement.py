# CLAHE mock contrast limiting
import numpy as np

img_dark = np.array([[10, 12], [11, 10]], dtype=np.uint8)
# Clip limit simulation
hist, bins = np.histogram(img_dark.flatten(), bins=4, range=[0, 256])
print("Histogram of dark image block:", hist)
