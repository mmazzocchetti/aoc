from itertools import pairwise

def parse_source(source):
    for line in source:
        yield line.strip().split(" ")

def is_line_safe(line):
    line_inc = None
    for a, b in pairwise(line):
        diff = int(a) - int(b)
        if line_inc is None:
            line_inc = diff > 0
        if (not 1 <= abs(diff) <= 3) or (line_inc is not bool(diff > 0)):
            return False
    else:
        return True

def part_1(source):
    return sum([1 for line in parse_source(source) if is_line_safe(line)])

def part_2(source):
    lines = parse_source(source)
    res = 0
    for line in lines:
        if is_line_safe(line):
            res += 1
        else:
            for i in range(0,len(line)):
                l_copy = line.copy()
                l_copy.pop(i-1)
                if is_line_safe(l_copy):
                    res+=1
                    break
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        source_lines = f.readlines()
    print("part 1", part_1(source_lines))
    print("part 2", part_2(source_lines))