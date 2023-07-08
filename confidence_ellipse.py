import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import  Ellipse

def eigsorted(cov):
    vals, vecs = np.linalg.eigh(cov)  # finding what is this
    order = vals.argsort()[::-1]      #
    return vals[order], vecs[:,order]


def plotting_ellipse(x_list, y_list):
    nstd = 2
    cov = np.cov(x_list, y_list)
    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))  # eigen vectors
    w, h = 2 * nstd * np.sqrt(vals)
    ell = Ellipse(xy=(np.mean(x_list), np.mean(y_list)),
              width=w, height=h,
              angle=theta, color='black')
    ell.set_facecolor("none")
    return ell


def main():
    x1 = [-13.25, -12.95, -12.9, -12.99, -13.25, -13.75, -13.51, -13.65]
    y1 = [-17.11, -17.13, -17.47, -17.63, -17.54, -17.49, -17.47, -16.99]
    x2 = [-11.21, -10.94, -10.74, -11.02, -11.21, -11.64, -11.54, -11.58]
    y2 = [9.12, 8.74, 8.64, 8.44, 8.2, 8.43, 8.64, 9.12]
    ellp_array = [0] * 20
    ellp_array[0]= plotting_ellipse(x1,y1)
    ellp_array[1] = plotting_ellipse(x2,y2)
    print(ellp_array)
    print(ellp_array[0])
    ax = plt.subplot()
    plt.scatter(x1,y1)
    plt.scatter(x2,y2)
    ax.add_artist(ellp_array[0])
    ax.add_artist(ellp_array[1])
    plt.show()


if __name__ == "__main__":
    main()

