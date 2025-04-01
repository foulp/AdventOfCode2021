import numpy as np
from pathlib import Path


def is_valid_path(path: list[str], one_small_multiple: bool):
    values, counts = np.unique(path, return_counts=True)
    nb_lower_multiples = 0
    for node, c in zip(values, counts):
        if node.islower() and c > 1:
            if not one_small_multiple or c > 2:
                return False
            nb_lower_multiples += 1
            if nb_lower_multiples > 1:
                return False
    return True


def find_paths(links: dict[str: list], current: str, current_path: list[str], one_small_multiple: bool):
    total_paths = 0
    neighbors = links[current]
    for n in neighbors:
        if n == 'end':
            total_paths += 1
        elif n == 'start':
            continue
        elif is_valid_path(current_path+[n], one_small_multiple):
            total_paths += find_paths(links, n, current_path+[n], one_small_multiple)
    return total_paths


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        graph = f.read().split('\n')
    links = {}
    for link in graph:
        a, b = link.split('-')
        links[a] = links.get(a, []) + [b]
        links[b] = links.get(b, []) + [a]

    print(f"The result of first star is {find_paths(links, 'start', ['start'], False)}")

    print(f"The result of second star is {find_paths(links, 'start', ['start'], True)}")
