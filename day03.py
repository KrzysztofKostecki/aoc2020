from typing import Tuple, List
from functools import reduce
from operator import add, mul

"""
--- Part One ---
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
"""


def check_slope(planet_map: List[str], r: int, d: int) -> int:
    trees: int = 0
    x: int = 0
    row_len = len(planet_map[0])
    for y in range(d, len(planet_map), d):
        x += r
        trees += 1 if planet_map[y][x % row_len] == "#" else 0
    return trees


with open("./inputs/day03.txt", "r") as f:
    planet_map = [row.strip() for row in f.readlines()]
    x: int = 0
    print(f"Result part 1 {check_slope(planet_map, r=3, d=1)}")

"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
"""

with open("./inputs/day03.txt", "r") as f:
    planet_map = [row.strip() for row in f.readlines()]
    x: int = 0
    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(
        f"Result part 2 {reduce(mul, [check_slope(planet_map, r=i[0], d=i[1]) for i in inputs])}"
    )
