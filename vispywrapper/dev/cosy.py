# %load_ext autoreload
# %autoreload 2
import numpy as np
import itertools

from vispywrapper.plot import get_figure, surfaces

# no color
if __name__ == "__main__":
    X = np.load("/home/matteo/Projects/masdiag/vispywrapper/data/nmr2dcosy.npz")
    x,y,I = X['x'], X['y'], X['I']

    figure = get_figure()
    surfaces(figure, 
             datasets=[(np.sqrt(I),x,y), 
                       (np.sqrt(I),x,y),
                       (np.sqrt(I),x,y),
                       (np.sqrt(I),x,y)])
    figure.show(run=True)

