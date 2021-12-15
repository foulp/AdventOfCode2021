from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        depths = pd.Series(map(int, f.read().split('\n')))

    result = (depths > depths.shift()).sum()
    print(f"The result of first star is {result}")

    windows = depths.rolling(window=3).sum()
    result = (windows > windows.shift()).sum()
    print(f"The result of second star is {result}")
