import numpy as np
from pathlib import Path
from scipy import ndimage


def get_flashes(grid):
    mask_flashes = grid == 10
    rows, cols = np.where(mask_flashes)
    neighbor_flashes = np.zeros(grid.shape).astype(int)
    for k, l in zip(rows, cols):
        flash_octopus = np.zeros(grid.shape)
        flash_octopus[k, l] = 1
        neighbor_flashes += (grid < 10) & ndimage.binary_dilation(flash_octopus, structure=struct).astype(int)
    grid = np.minimum(10, grid + neighbor_flashes)
    return grid, mask_flashes, neighbor_flashes


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        grid = np.array([list(map(int, line)) for line in f.read().split('\n')])

    struct = ndimage.generate_binary_structure(2, 2)
    struct[1, 1] = False

    total_flashes = 0
    step = 0
    while grid.sum().sum() != 0:
        step += 1
        grid += 1
        grid, mask_flashes, neighbor_flashes = get_flashes(grid)
        grid[mask_flashes] = 11
        if step <= 100:
            total_flashes += mask_flashes.sum().sum()
        while neighbor_flashes.sum().sum():
            old_flashes = grid == 11
            grid, mask_flashes, neighbor_flashes = get_flashes(grid)
            grid[mask_flashes | old_flashes] = 11
            if step <= 100:
                total_flashes += mask_flashes.sum().sum()
        grid[grid > 9] = 0

    print(f"The result of first star is {total_flashes}")

    print(f"The result of second star is {step}")
