input_path = 'input.txt'

MARKER = 'X'


def chop_board(board):
    lines = board.split('\n')
    
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        
    return lines


def get_score(board, last_number):
    sum = 0
    
    for line in board:
        for number in line:
            if not number == MARKER:
                sum += int(number)
                
    return sum * int(last_number)


def check_win(board):
    winning_line = [MARKER for x in range(len(board))]
    
    if winning_line in board:
        return True
    
    if winning_line in [list(row) for row in zip(*board)]:
        return True
    
    return False


def mark_number(board, number):
    new_board = board.copy()
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if not new_board[i][j] == MARKER and new_board[i][j] == number:
                new_board[i][j] = MARKER
                return new_board
    return new_board


def play_bingo(numbers, boards):
    for number in numbers:
        for i in range(len(boards)):
            boards[i] = mark_number(boards[i], number)
            if check_win(boards[i]):
                return (boards[i], number)


if __name__ == '__main__':
    numbers = []
    boards = []
    
    with open(input_path) as input_data:
        [numbers, *boards] = input_data.read().split('\n\n')
        numbers = numbers.split(',')
        for i in range(len(boards)):
            boards[i] = chop_board(boards[i])

    first_winner, last_number = play_bingo(numbers, boards)

    print(get_score(first_winner, last_number))
