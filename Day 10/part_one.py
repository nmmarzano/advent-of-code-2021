input_path = 'input.txt'

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
opening = ['(', '[', '{', '<']
closing = {'(': ')', '[': ']', '{': '}', '<': '>'}


def first_corrupted_char(line):
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            if char == closing[stack[-1]]:
                stack.pop()
            else:
                return char
    

if __name__ == '__main__':
    with open(input_path) as input_data:
        lines = input_data.read().split('\n')

    score = 0
    for line in lines:
        illegal_char = first_corrupted_char(line)
        if illegal_char is not None:
            score += scores[illegal_char]

    print(score)
