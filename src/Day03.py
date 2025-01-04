from pathlib import Path
import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        diagnostic_bits = f.read().split('\n')
    diagnostic_bits = np.array([list(map(int, bit)) for bit in diagnostic_bits])

    sums = np.sum(diagnostic_bits, axis=0)
    epsilon_rate = int(''.join(map(str, map(int, sums > diagnostic_bits.shape[0] / 2))), 2)
    gamma_rate = 2**diagnostic_bits.shape[1] - 1 - epsilon_rate

    print(f"The result of first star is {epsilon_rate * gamma_rate}")

    print(f"The result of second star is {0}")
