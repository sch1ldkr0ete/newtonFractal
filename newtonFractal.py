import numpy as np
import scipy.misc as smp


def f(roots, z):
    result = 1.
    for root in roots:
        result *= (z - root)
    return result

# roots of the complex polynomial
roots = np.array([1., complex(-.5, 3. ** .5 * .5),
                  complex(-.5, -3. ** .5 * .5)])

# size of image in pixels
SIZE_X = 1000  # x size
SIZE_Y = 1000  # y size
# coordinate size
X_A = -1.
X_B = 1.
Y_A = -1.
Y_B = 1.
# maximum number of iterations allowed for finding a root
MAX_ITERS = 25
# maximum error
EPS = 1.e-5
# step size
H = 1.e-5

# array for the pixel values
pixels = np.zeros(shape=(SIZE_X, SIZE_Y, 3), dtype=np.uint8)

# iterate over the pixels and use them as starting point for the newton
# iteration
for img_x in range(SIZE_X):
    x = X_A + img_x * (X_B - X_A) / (SIZE_X - 1)
    for img_y in range(SIZE_Y):
        y = Y_A + img_y * (Y_B - Y_A) / (SIZE_Y - 1)
        z = complex(x, y)  # starting point
        # newtons method
        for i in range(MAX_ITERS):
            f_prime = ((f(roots, z + complex(H, H)) - f(roots, z))
                       / complex(H, H))
            z_0 = z - f(roots, z) / f_prime
            if abs(z_0 - roots[0]) < EPS:
                pixels[img_x, img_y] = [255 - i * 10, 0, 0]
                break
            elif abs(z_0 - roots[1]) < EPS:
                pixels[img_x, img_y] = [0, 255 - i * 10, 0]
                break
            elif abs(z_0 - roots[2]) < EPS:
                pixels[img_x, img_y] = [0, 0, 255 - i * 10]
                break
            z = z_0

# build image
smp.imsave('newtonFractal.png', pixels)
#img = smp.toimage(pixels)
#img.show()
