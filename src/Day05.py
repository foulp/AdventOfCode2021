from pathlib import Path
from collections import defaultdict

import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        lines = f.read().split('\n')
    grid = defaultdict(lambda: 0, {})
    for line in lines:
        start, end = line.split(' -> ')
        x_start, y_start = map(int, start.split(','))
        x_end, y_end = map(int, end.split(','))
        if x_start == x_end:
            for y in range(min(y_start, y_end), max(y_start, y_end)+1):
                grid[(x_start, y)] += 1
        elif y_start == y_end:
            for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
                grid[(x, y_start)] += 1

    print(f"The result of first star is {len(grid) - list(grid.values()).count(1)}")

    for line in lines:
        start, end = line.split(' -> ')
        x_start, y_start = map(int, start.split(','))
        x_end, y_end = map(int, end.split(','))
        if x_start != x_end and y_start != y_end:
            length = abs(y_start - y_end)
            for i in range(length + 1):
                grid[(x_start + i * np.sign(x_end - x_start), y_start + i * np.sign(y_end - y_start))] += 1
    print(f"The result of second star is {len(grid) - list(grid.values()).count(1)}")
