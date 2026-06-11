# Color conversion mock
import numpy as np

pixel_rgb = [100, 120, 150]
r, g, b = [c/255.0 for c in pixel_rgb]
mx = max(r, g, b)
v = mx
print(f"RGB {pixel_rgb} -> Value (V) in HSV: {v:.4f}")
