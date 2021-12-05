import pathlib
import pytest
import aoc202103 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly"""
    print(example1)
    assert example1 == [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0]
        ]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 198

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 230