from collections import defaultdict


def read_input_file(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def read_values_file(values_file_name):
    with open(values_file_name, 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]
    return dict([(ch, int(score)) for ch, score in lines])


def get_abbreviations(word):
    abbrevs = []
    word = word.upper().replace("'", "")
    words = word.split()
    for i, w in enumerate(words):
        for j, c in enumerate(w):
            if j == 0:
                abbrev = c
            elif j == 1:
                abbrev += w[j]
            elif c.isalpha():
                abbrev += w[j]
            if len(abbrev) == 3:
                abbrevs.append((abbrev, i, j))
                break
    return abbrevs


def get_score(abbrev, word_positions, values):
    score = values[abbrev[1]] + values[abbrev[2]]
    if word_positions[1] == 0:
        score = 0
    elif word_positions[2] == len(word_positions[3])-1 and abbrev[2] != 'E':
        score += 5
    else:
        pos_score = 1 if word_positions[2] == 1 else (2 if word_positions[2] == 2 else 3)
        score += pos_score + values[abbrev[2]]
    return score


def main():
    input_file_name = input("Enter the input file name: ")
    output_file_name = input_file_name.split('.')[0] + '_abbrevs.txt'
    values_file_name = 'values.txt'
    words = read_input_file(input_file_name)
    values = read_values_file(values_file_name)
    used_abbrevs = defaultdict(list)
    for word in words:
        abbrevs = get_abbreviations(word)
        for abbrev in abbrevs:
            used_by = [w for w, abbs in used_abbrevs.items() if abbrev[0] in abbs]
            if len(used_by) == 0:
                used_abbrevs[word].append(abbrev[0])
            elif word not in used_by:
                used_abbrevs[word].append(abbrev[0])
    with open(output_file_name, 'w') as f:
        for word in words:
            f.write(word + '\n')
            abbrevs = get_abbreviations(word)
            scores = []
            for abbrev in abbrevs:
                if abbrev[0] in used_abbrevs[word]:
                    word_positions = [abbrev[0][0], abbrev[0][1], abbrev[0][2], word]
                    score = get_score(abbrev[0], word_positions, values)
                    scores.append((abbrev[0], score))
            if len(scores) > 0:
                min_score = min([score for abbrev, score in scores])
                best_abbrevs = [abbrev for abbrev, score in scores if score == min_score]
                f.write(' '.join(best_abbrevs) + '\n')
            else:
                f.write('\n')


if __name__ == '__main__':
    main()
