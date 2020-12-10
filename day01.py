from typing import Tuple, Set

"""
--- Part One ---
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

entries = Set[int]
with open("./inputs/day01.txt", "r") as f:
    entries = set([int(entry) for entry in f.readlines()])


def sum_to(number: int) -> Tuple[int, int]:
    for e in entries:
        if number - e in entries:
            return e, number - e
    raise Exception(f"Couldn't find two numbers that sum up to {number}")


a, b = sum_to(2020)
print(a * b)

"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

for e in entries:
    try:
        x, y = sum_to(2020 - e)
        print(e * x * y)
        break
    except Exception as error:
        pass
