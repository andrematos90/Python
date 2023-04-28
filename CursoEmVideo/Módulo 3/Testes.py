import numpy as np

def mandelbrot(width, height, zoom=1, x_off=0, y_off=0, max_iter=1000):
    x, y = np.meshgrid(np.linspace(-2.5, 1.5, width), np.linspace(-2, 2, height))
    c = x + y * 1j
    z = np.zeros_like(c)
    output = np.zeros_like(c, dtype=np.int32)
    for i in range(max_iter):
        mask = np.abs(z) < 2
        output[mask] = i
        z[mask] = z[mask] ** 2 + c[mask]
    return output

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.imshow(mandelbrot(1920, 1080, zoom=1e3))
    plt.show()
