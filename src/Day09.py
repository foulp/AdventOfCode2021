from pathlib import Path
import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        heightmap = np.array([list(map(int, line)) for line in f.read().split('\n')])

    risk_level = 0
    bassins_idx = {}
    idx_bassins = {}
    for (x, y), h in np.ndenumerate(heightmap):
        if h == 9:
            continue

        is_low_point = True
        neigbors_bassins = []
        if x > 0:
            is_low_point = min(is_low_point, heightmap[x-1, y] > h)
            if (x-1, y) in idx_bassins:
                neigbors_bassins.append(idx_bassins[(x-1, y)])
        if x < heightmap.shape[0] - 1:
            is_low_point = min(is_low_point, heightmap[x+1, y] > h)
            if (x+1, y) in idx_bassins:
                neigbors_bassins.append(idx_bassins[(x+1, y)])
        if y > 0:
            is_low_point = min(is_low_point, heightmap[x, y-1] > h)
            if (x, y-1) in idx_bassins:
                neigbors_bassins.append(idx_bassins[(x, y-1)])
        if y < heightmap.shape[1] - 1 :
            is_low_point = min(is_low_point, heightmap[x, y+1] > h)
            if (x, y+1) in idx_bassins:
                neigbors_bassins.append(idx_bassins[(x, y+1)])

        if is_low_point:
            risk_level += h+1

        final_bassin = min(neigbors_bassins, default=max(bassins_idx, default=0) + 1)
        idx_bassins[(x, y)] = final_bassin
        bassins_idx[final_bassin] = bassins_idx.get(final_bassin, []) + [(x, y)]
        for b in neigbors_bassins:
            if b != final_bassin:
                for i, j in bassins_idx[b]:
                    idx_bassins[(i, j)] = final_bassin
                    bassins_idx[final_bassin].append((i, j))
                del bassins_idx[b]

    print(f"The result of first star is {risk_level}")

    print(f"The result of second star is {np.prod(sorted([len(bassins_idx[b]) for b in bassins_idx])[-3:])}")
