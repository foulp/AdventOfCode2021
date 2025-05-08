from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        template, rules = f.read().split('\n\n')

    rules = {r.split(' -> ')[0]: r.split(' -> ')[1] for r in rules.split('\n')}

    for j in range(10):
        new_template = ""
        for i, c in enumerate(template[:-1]):
            new_template += c
            if template[i:i+2] in rules:
                new_template += rules[template[i:i+2]]
        new_template += template[-1]
        template = str(new_template)
        print(f"End of loop {j}")

    counts = [template.count(v) for v in set(template)]
    print(f"The result of first star is {max(counts) - min(counts)}")

    print(f"The result of second star is {0}")
