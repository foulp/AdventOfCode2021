from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        lanternfish = pd.Series(map(int, f.read().split(','))).value_counts()

    for i in range(-1, 9):
        if i not in lanternfish:
            lanternfish.loc[i] = 0

    for day in range(256):
        if day == 80:
            print(f"The result of first star is {lanternfish.sum()}")

        new_fish = lanternfish.loc[0]
        lanternfish = pd.Series(lanternfish.values, index=lanternfish.index - 1)
        lanternfish.loc[6] += lanternfish.loc[-1]
        lanternfish = lanternfish.drop(index=-1)
        lanternfish.loc[8] = new_fish

    print(f"The result of second star is {lanternfish.sum()}")
