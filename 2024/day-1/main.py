from collections import Counter


def parse_source(source):
    l1 = []
    l2 = []
    for line in source:
        a,b  = line.strip().split("   ")
        l1.append(int(a))
        l2.append(int(b))
    return l1, l2

def part_1(source):
    l1,l2 = parse_source(source)
    return sum(abs(a-b) for a,b in zip(sorted(l1), sorted(l2), strict=True))

def part_2(source):
    l1,l2 = parse_source(source)
    c2 = Counter(l2)
    return sum(x * c2[x] for x in l1)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print("part 1", part_1(lines))
    print("part 2", part_2(lines))