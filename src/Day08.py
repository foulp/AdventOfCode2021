from pathlib import Path


def get_mapping(digits):
    displays = {  # lengths
        'abcefg': 0,  # 6
        'cf': 1,  # 2
        'acdeg': 2,  # 5
        'acdfg': 3,  # 5
        'bcdf': 4,  # 4
        'abdfg': 5,  # 5
        'abdefg': 6,  # 6
        'acf': 7,  # 3
        'abcdefg': 8,  # 7
        'abcdfg': 9  # 6
    }
    # La lettre dans le pattern de longueur 3 mais pas dans celui de longueur 2 est "a"
    # Les trois lettres uniques dans les trois patterns de longueur 6 sont "c", "d" et "e"
    # Ce qui permet donc d'identifier "c" présent dans le pattern de longueur 2
    # Et donc "f" la lettre restante de ce pattern de longueur 2
    # Et donc "d" présent aussi dans le pattern de longueur 4 (mais pas "e"), et donc "e"
    # Et donc "b" présent dans le pattern de longueur 4 parmi les deux lettres restantes
    segment_mapping = {}
    pattern3 = next(d for d in digits if len(d) == 3)
    pattern2 = next(d for d in digits if len(d) == 2)
    pattern4 = next(d for d in digits if len(d) == 4)
    segment_mapping['a'] = list(set(pattern3) - set(pattern2))[0]
    pattern6 = [d for d in digits if len(d) == 6]
    cde = set([d for d in ''.join(pattern6) if ''.join(pattern6).count(d) == 2])
    segment_mapping['c'] = list(cde & set(pattern2))[0]
    segment_mapping['f'] = list(set(pattern2) - set(segment_mapping['c']))[0]
    segment_mapping['d'] = list(set(pattern4) & cde - set(segment_mapping['c']))[0]
    segment_mapping['e'] = list(cde - set(segment_mapping['c']) - set(segment_mapping['d']))[0]
    segment_mapping['b'] = list(set(pattern4) - cde - set(segment_mapping['f']))[0]
    segment_mapping['g'] = list(set('abcdefg') - set(segment_mapping.values()))[0]

    segment_mapping = {
        ''.join(sorted([segment_mapping[char] for char in d])): displays[d] for d in displays
    }
    return segment_mapping


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        inputs = f.read().split('\n')

    result = 0
    for display in inputs:
        patterns, output_value = display.split(' | ')
        result += sum(1 for digit in map(len, output_value.split()) if digit in (2, 3, 4, 7))
    print(f"The result of first star is {result}")

    result = 0
    for display in inputs:
        patterns, output_value = display.split(' | ')
        digits = patterns.split()
        mapping = get_mapping(digits)
        result += int(''.join(str(mapping[''.join(sorted(digit))]) for digit in output_value.split()))
    print(f"The result of second star is {result}")
