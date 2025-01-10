from pathlib import Path
import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        crabs = list(map(int, f.read().split(',')))
        
    final_pos = np.median(crabs)
    print(f"The result of first star is {sum(abs(final_pos - x) for x in crabs)}")

    fuel = min(sum(abs(x - h) * (abs(x - h) + 1) / 2 for x in crabs) for h in range(min(crabs), max(crabs)+1))
    print(f"The result of second star is {fuel}")
