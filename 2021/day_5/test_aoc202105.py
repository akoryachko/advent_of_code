import pathlib
import pytest
import aoc202105 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example):
    """Test that input is parsed properly"""
    print(example)
    assert example == [
        '0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2',
        ]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 5

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == 12