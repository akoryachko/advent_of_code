import pathlib
import sys

DEPTH_DIRECTIONS = {'down': 1, 'up': -1}

def parse(puzzle_input):
    """Parse input"""
    data = [(s.split()[0], int(s.split()[1])) for s in puzzle_input.split('\n')]
    return data

def part1(data):
    """Solve part 1"""
    horizontal_position = sum([inc for dir, inc in data if dir == 'forward'])
    depth = sum([inc*DEPTH_DIRECTIONS.get(dir, 0) for dir, inc in data])
    return horizontal_position*depth

def part2(data):
    """Solve part 2"""
    aim, horizontal_position, depth = 0, 0, 0
    for dir, val in data:
        if dir == 'forward':
            horizontal_position += val
            depth += val*aim
        else:
            aim += val*DEPTH_DIRECTIONS.get(dir, 0)
            
    return horizontal_position*depth

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