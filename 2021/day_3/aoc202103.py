import pathlib
import sys
import numpy as np

def bin2dec(a) -> int:
    return sum(a*2**np.arange(len(a)-1,-1,-1))

def get_the_rating_code(m, co2=False, col=0):
    if m.shape[0] == 1:
        return m[0,:]
    winner = int((sum(m[:,col])*2 >= m.shape[0]) != co2)
    return get_the_rating_code(m[m[:, col] == winner,:], co2, col+1)

def parse(puzzle_input):
    """Parse input"""
    data = [[int(v) for v in s] for s in puzzle_input.split('\n')]
    return data

def part1(data):
    """Solve part 1"""
    gamma_code = (sum(np.array(data))*2/len(data)).astype(int)
    
    gamma, epsilon = (bin2dec(code) for code in (gamma_code, 1-gamma_code))
    return gamma*epsilon

def part2(data):
    """Solve part 2"""
    np_data = np.array(data)

    oxygen_code = get_the_rating_code(np_data)
    co2_code = get_the_rating_code(np_data, co2=True)

    return np.prod([bin2dec(c) for c in (oxygen_code, co2_code)])

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