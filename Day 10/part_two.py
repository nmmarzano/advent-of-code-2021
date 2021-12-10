input_path = 'input.txt'

scores = {')': 1, ']': 2, '}': 3, '>': 4}
opening = ['(', '[', '{', '<']
closing = {'(': ')', '[': ']', '{': '}', '<': '>'}


def find_closing_characters(line):
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            if char == closing[stack[-1]]:
                stack.pop()
            else:
                return

    closing_characters = []

    while len(stack) > 0:
        closing_characters.append(closing[stack.pop()])

    return ''.join(closing_characters)


def get_score(characters):
    score = 0
    for char in characters:
        score = score * 5 + scores[char]
    return score
    

if __name__ == '__main__':
    with open(input_path) as input_data:
        lines = input_data.read().split('\n')

    final_scores = []
    for line in lines:
        closing_characters = find_closing_characters(line)
        if closing_characters is not None:
            final_scores.append(get_score(closing_characters))

    final_scores.sort()
    print(final_scores[int(len(final_scores) / 2)])
