from pathlib import Path
import numpy as np

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        inputs = f.read().split('\n\n')
        drawn_numbers, boards = inputs[0], inputs[1:]

    drawn_numbers = map(int, drawn_numbers.split(','))
    boards = [np.array([list(map(int, line.split())) for line in b.split('\n')]) for b in boards]
    boards_checks = [np.zeros(b.shape) for b in boards]
    winning_scores = {}
    winnings_order = []
    
    for n in drawn_numbers:
        for i, b in enumerate(boards):
            if i in winning_scores:
                continue
            idx = np.where(b == n)
            boards_checks[i][idx] = 1

            if any(boards_checks[i].sum(axis=1) == b.shape[0]) or any(boards_checks[i].sum(axis=0) == b.shape[1]):
                winning_scores[i] = n * (b * (1-boards_checks[i])).sum()
                winnings_order.append(i)
        if len(winning_scores) == len(boards):
            break

    print(f"The result of first star is {winning_scores[winnings_order[0]]}")

    print(f"The result of second star is {winning_scores[winnings_order[-1]]}")
