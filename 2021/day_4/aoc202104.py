import pathlib
import sys
import numpy as np

class Bingo:

    def __init__(self, rows):
        self.card = np.array([[int(n) for n in row.split()] for row in rows], dtype=np.byte)
        self.hits = np.zeros_like(self.card)
        self.number_of_elements_in_row = self.card.shape[0]

    def __repr__(self):
        return f'Board\n {self.card}\nCurrent State\n{self.hits}'

    def check_number(self, draw:int):
        self.hits[self.card == draw] = 1
        most_hits = max(self.hits.sum(axis=a).max() for a in [0, 1])
        return most_hits == self.number_of_elements_in_row
    
    def calculate_score(self, draw:int):
        unmarked_numbers = self.card[self.hits == 0]
        return sum(unmarked_numbers)*draw


def parse(puzzle_input):
    """Parse input"""
    rows = puzzle_input.split('\n')

    data = [[int(n) for n in rows.pop(0).split(',')]]

    while rows:
        bingo_block = rows[1:6]
        data.append(bingo_block)
        del rows[:6]
    return data

def part1(data):
    """Solve part 1"""
    draws = data[0]
    boards = [Bingo(board) for board in data[1:]]

    for draw in draws:
        for board in boards:
            if board.check_number(draw):
                return board.calculate_score(draw)

def part2(data):
    """Solve part 2"""
    draws = data[0]
    boards = [Bingo(board) for board in data[1:]]
    boards_unfinished = np.ones(len(boards), dtype=np.byte)

    for draw in draws:
        for board in boards:
            if board.check_number(draw):
                boards_unfinished[boards.index(board)] = 0
                if sum(boards_unfinished) == 0:
                    return board.calculate_score(draw)

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))