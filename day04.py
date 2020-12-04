from typing import Tuple, List
from functools import reduce
from operator import add, mul
import re

"""
--- Part One ---
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
"""


def check_required_fields(password: str) -> int:
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for field in required_fields:
        if not re.search(f"{field}:\\S*", password):
            return 0
    return 1


with open("./inputs/day04.txt", "r") as f:
    print(
        reduce(
            add,
            [
                check_required_fields(password.strip())
                for password in re.split("\n\n", f.read())
            ],
        )
    )

"""
--- Part Two ---
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
"""


def check_required_fields_2(password: str) -> int:
    required_fields = {
        "byr": r"19[2-9][0-9]|200[0-2]",
        "iyr": r"201[0-9]|2020",
        "eyr": r"202[0-9]|2030",
        "hgt": r"1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in",
        "hcl": r"\#[0-9a-f]{6}",
        "ecl": r"amb|blu|brn|gry|grn|hzl|oth",
        "pid": r"\d{9}",
    }
    for field, pattern in required_fields.items():
        if not re.search(fr"{field}:{pattern}(\s|$)", password):
            return 0
    return 1


with open("./inputs/day04.txt", "r") as f:
    print(
        reduce(
            add,
            [
                check_required_fields_2(password.strip())
                for password in re.split("\n\n", f.read())
            ],
        )
    )
