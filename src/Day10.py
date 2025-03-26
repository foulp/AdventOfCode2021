from pathlib import Path

closing_char = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
syntax_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def is_corrupted(line: str) -> (bool, str):
    meet_opening: list[str] = []
    for char in line:
        if char in closing_char:
            meet_opening.append(char)
        elif len(meet_opening) == 0:
            return True, char
        elif char != closing_char[meet_opening[-1]]:
            return True, char
        else:
            meet_opening.pop()
    return False, ''.join([closing_char[c] for c in meet_opening[::-1]])

def incomplete_score(closing_chars: str) -> int:
    score = 0
    for c in closing_chars:
        score *= 5
        score += autocomplete_points[c]
    return score

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        navigation_subsystem = f.read().split('\n')

    incorrect_score = 0
    incomplete_scores = []
    for i, line in enumerate(navigation_subsystem):
        a, b = is_corrupted(line)
        if a:
            incorrect_score += syntax_points[b]
        else:
            if len(b):
                incomplete_scores.append(incomplete_score(b))

    print(f"The result of first star is {incorrect_score}")

    print(f"The result of second star is {sorted(incomplete_scores)[len(incomplete_scores) // 2]}")
