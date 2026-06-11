# Topic 3: Image Sharpening

Sharpening highlights edges (intensity transitions) using high-pass filters.
- **Laplacian Filter**: Second-derivative isotropic operator:
  $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
- **High-Boost & Unsharp Masking**: Adding high-frequency details mask back to original.
