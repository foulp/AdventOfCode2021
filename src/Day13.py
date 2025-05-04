import numpy as np
import re
from scipy.sparse import coo_matrix
from pathlib import Path


def fold(array, axis, value):
    halfway = array.shape[axis] // 2

    if axis == 1:
        if value != halfway:
            shape_to_add = 2 * (value - halfway)
            array = np.concatenate([array, np.zeros((array.shape[1-axis], shape_to_add))], axis=axis)
            halfway = array.shape[axis] // 2
        a1 = array[:, :halfway]
        a2 = array[:, halfway + 1:]
    else:
        if value != halfway:
            shape_to_add = 2 * (value - halfway)
            array = np.concatenate([array, np.zeros((shape_to_add, array.shape[1-axis]))], axis=axis)
            halfway = array.shape[axis] // 2
        a1 = array[:halfway, :]
        a2 = array[halfway + 1:, :]

    a2 = np.flip(a2, axis=axis)
    return np.minimum(1, a1 + a2)


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        dots, folds = f.read().split('\n\n')

    dots = np.array([list(map(int, dot.split(','))) for dot in dots.split('\n')])
    folds = [re.search(r'(\w)=(\d+)', fold).groups() for fold in folds.split('\n')]
    folds = [(1 if axis == 'x' else 0, int(value)) for axis, value in folds]

    sheet = coo_matrix(([1]*dots.shape[0], (dots[:, 1], dots[:, 0]))).toarray()

    print(f"The result of first star is {fold(sheet, folds[0][0], folds[0][1]).sum()}")

    for f in folds:
        sheet = fold(sheet, f[0], f[1])
    sheet = '\n'.join(''.join(row) for row in sheet.astype(int).astype(str)).replace('0', '.').replace('1', '#')
    print(f"The result of second star is \n{sheet}")
