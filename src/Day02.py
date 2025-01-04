from pathlib import Path

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        commands = f.read().split('\n')

    depth, horizontal = 0, 0
    for command in commands:
        direction, value = command.split()
        value = int(value)
        if direction == 'forward':
            horizontal += value
        elif direction == 'down':
            depth += value
        else:
            depth -= value
    print(f"The result of first star is {depth * horizontal}")

    depth, horizontal, aim = 0, 0, 0
    for command in commands:
        direction, value = command.split()
        value = int(value)
        if direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        else:
            horizontal += value
            depth += aim * value
    print(f"The result of second star is {depth * horizontal}")
