from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        diagnostic_bits = f.read().split('\n')
    diagnostic_bits = pd.DataFrame([list(map(int, bit)) for bit in diagnostic_bits])
    sums = diagnostic_bits.sum(axis=0)
    epsilon_rate = int(''.join(map(str, map(int, sums > diagnostic_bits.shape[0] / 2))), 2)
    gamma_rate = 2**diagnostic_bits.shape[1] - 1 - epsilon_rate
    print(f"The result of first star is {epsilon_rate * gamma_rate}")

    ogr = diagnostic_bits.copy(deep=True)
    csr = diagnostic_bits.copy(deep=True)
    i = 0
    while ogr.shape[0] > 1 or csr.shape[0] > 1:
        ogr = ogr[ogr[i].value_counts().sort_index(ascending=False).idxmax() == ogr[i]]
        csr = csr[csr[i].value_counts().sort_index(ascending=True).idxmin() == csr[i]]
        i += 1
    ogr = int(''.join(map(str, map(int, ogr.iloc[0]))), 2)
    csr = int(''.join(map(str, map(int, csr.iloc[0]))), 2)
    print(f"The result of second star is {ogr*csr}")
