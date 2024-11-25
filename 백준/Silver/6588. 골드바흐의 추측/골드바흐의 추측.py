import sys

input = sys.stdin.readline
print = sys.stdout.write

soe = [True] * 1000000
for i in range(3, 1000000, 2):
    if soe[i]: soe[i*i::i*2]= [False] * len(soe[i*i::i*2])
result_soe = [i for i in range(3, 1000000, 2) if soe[i]]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        flag = True
        for i in result_soe:
            if soe[n - i]:
                print(f"{n} = {i} + {n - i}\n")
                flag = False
                break
        if flag:
            print("Goldbach's conjecture is Wrong.\n")