import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.textpath
import matplotlib.patches
from matplotlib.font_manager import FontProperties
import numpy as np


def main():
    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mollweide(central_longitude=90))

    ax.coastlines()
    ax.gridlines()
    # ax.stock_img()
    # generate a matplotlib path representing the word "cartopy"
    fp = FontProperties(family='Consolas', weight='bold')
    logo_path = matplotlib.textpath.TextPath((-360, -50), 'HOUCZ', size=1, prop=fp)
    # scale the letters up to sensible longitude and latitude sizes
    logo_path._vertices *= np.array([70, 170])

    # add a background image
    im = ax.stock_img()
    # clip the image according to the logo_path. mpl v1.2.0 does not support
    # the transform API that cartopy makes use of, so we have to convert the
    # projection into a transform manually
    plate_carree_transform = ccrs.PlateCarree()._as_mpl_transform(ax)
    im.set_clip_path(logo_path, transform=plate_carree_transform)

    # add the path as a patch, drawing black outlines around the text
    patch = matplotlib.patches.PathPatch(logo_path,
                                         facecolor='None', edgecolor='black', linewidth=5,
                                         transform=ccrs.PlateCarree())
    ax.add_patch(patch)

    plt.savefig('bg.jpg')


if __name__ == '__main__':
    main()
