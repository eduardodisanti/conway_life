import matplotlib.pyplot as plt

import numpy as np


def randomGrid(N, probabilty=0.1):
    """creates a grid of NxN with random cells"""

    cell_prob = 1 - probabilty

    return np.random.choice([1, 0], N * N, p=[cell_prob, probabilty]).reshape(N, N)

def life_step(grid, N):

        newGrid = grid.copy()
        for i in range(1,N):
            for j in range(1,N):

                # compute neighbor sum
                neigh = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                             grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                             grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                             grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)


                # Conway's rules for current timestep
                if grid[i, j] == 1:
                    if (neigh < 2) or (neigh > 3):
                        newGrid[i, j] = 0
                else:
                    if neigh == 3:
                        newGrid[i, j] = 1

        grid[:] = newGrid[:]
        return grid,

def main():

    # set grid size
    N = 50

    updateInterval = 50

    grid = np.array([])

    grid = randomGrid(N)

        # set up animation
    fig, ax = plt.subplots()
    running = True
    img = ax.imshow(grid, interpolation='nearest', cmap="gray")

    while running:

        grid = life_step(grid, N)

        ax.imshow(img, cmap="gray")
        plt.show()

if __name__ == '__main__':
    main()