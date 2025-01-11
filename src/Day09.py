from pathlib import Path
import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        heightmap = np.array([list(map(int, line)) for line in f.read().split('\n')])

    risk_level = 0
    for (x, y), h in np.ndenumerate(heightmap):
        high_neighbors = 0
        if x > 0 and heightmap[x-1, y] <= h:
            continue
        if x < heightmap.shape[0] - 1 and heightmap[x+1, y] <= h:
            continue
        if y > 0 and heightmap[x, y-1] <= h:
            continue
        if y < heightmap.shape[1] - 1 and heightmap[x, y+1] <= h:
            continue
        risk_level += h+1

    print(f"The result of first star is {risk_level}")

    print(f"The result of second star is {0}")
