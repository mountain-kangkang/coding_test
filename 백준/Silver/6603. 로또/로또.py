import itertools
import sys
input = sys.stdin.read

def sol(test:list):
    comb = itertools.combinations(test, 6)

    for c in comb:
        print(*c)

data = input().splitlines()

for i in range(len(data) - 1):
    sol(list(map(int, data[i].split()))[1:])
    print()