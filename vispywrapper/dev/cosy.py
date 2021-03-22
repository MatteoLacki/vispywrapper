import numpy as np
from math import sqrt, ceil, floor
import itertools

from vispywrapper.plot import get_figure, surfaces


if __name__ == "__main__":
    X = np.load("/home/matteo/Projects/masdiag/vispywrapper/data/nmr2dcosy.npz")
    x,y,I = X['x'], X['y'], X['I']
    # surface_plot(np.sqrt(I))
    # surface_plot(np.sqrt(I), x, y)
    # figure = get_figure()
    # surfaces(figure, datasets=[(np.sqrt(I),x,y), 
    #                            (np.sqrt(I),x,y),
    #                            (np.sqrt(I),x,y),
    #                            (np.sqrt(I),x,y)])
    # figure.show(run=True)

    figure = get_figure()
    surfaces(figure, datasets=[(np.sqrt(I),x,y), 
                               (np.sqrt(I),x,y),
                               (np.sqrt(I),x,y),
                               (np.sqrt(I),x,y)],
             ncol=4, nrow=1)
    figure.show(run=True)