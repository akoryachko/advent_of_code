import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    data = puzzle_input.split('\n')
    return data

def sorted_range(a1, a2):
    direction = -1 if a1 > a2 else 1
    return range(a1, a2 + direction, direction)

def add_to_count(vals, count):
    for v in vals:
        count[v] = count.get(v, 0) + 1
    return count

def part1(data):
    """Solve part 1"""
    count = {}
    for line in data:
        x1, y1, x2, y2 = (int(v) for v in line.replace(' -> ',',').split(','))
        if x1 == x2:
            vals = [(x1, y) for y in sorted_range(y1, y2)]
            count = add_to_count(vals, count)
        elif y1 == y2:
            vals = [(x, y1) for x in sorted_range(x1, x2)]
            count = add_to_count(vals, count)
        else:
            continue

    return len([v for v in count.values() if v > 1])

def part2(data):
    """Solve part 2"""
    count = {}
    for line in data:
        x1, y1, x2, y2 = (int(v) for v in line.replace(' -> ',',').split(','))
        if x1 == x2:
            vals = [(x1, y) for y in sorted_range(y1, y2)]
            count = add_to_count(vals, count)
        elif y1 == y2:
            vals = [(x, y1) for x in sorted_range(x1, x2)]
            count = add_to_count(vals, count)
        else:
            vals = [(x, y) for x, y in zip(sorted_range(x1, x2), sorted_range(y1, y2))]
            count = add_to_count(vals, count)

    return len([v for v in count.values() if v > 1])

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