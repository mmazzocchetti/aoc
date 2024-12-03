import re
from operator import mul
from pathlib import Path

def part_1(source):
    operations = re.findall(r"mul\(\d+,\d+\)", source)
    exp = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(mul(*map(int, exp.findall(op)[0])) for op in operations)

def part_2(source):
    operations = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", source)
    exp = re.compile(r"mul\((\d+),(\d+)\)")
    res = 0
    enable = True
    for op in operations:
        if op == "do()":
            enable = True
        elif op == "don't()":
            enable = False
        elif enable:
            res += mul(*map(int, exp.findall(op)[0]))
    return res


if __name__ == "__main__":
    source = Path("input.txt").read_text()
    print("part 1", part_1(source))
    print("part 2", part_2(source))
