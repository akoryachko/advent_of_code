import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    data = [int(s) for s in puzzle_input.split('\n')]
    return data

def part1(data):
    """Solve part 1"""
    res = sum([1 for n in range(len(data) - 1) if data[n+1] > data[n]])
    return res

def part2(data):
    """Solve part 2"""
    averages = [sum([data[m] for m in range(n, n+3)]) for n in range(len(data) - 2)]
    res = part1(averages)
    return res

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