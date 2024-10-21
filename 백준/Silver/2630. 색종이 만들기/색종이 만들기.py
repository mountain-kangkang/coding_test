import sys

limit = [2, 4, 8, 16, 32, 64, 128]
white = 0
blue = 0

def sol(paper:list):
    global white, blue

    if all(all(p == 1 for p in row) for row in paper):
        blue += 1
        return
    elif all(all(p == 0 for p in row) for row in paper):
        white += 1
        return
    else:
        size = len(paper)
        one, two, three, four = [], [], [], []
        for i in range(size):
            if (size // 2) > i:
                one.append(paper[i][0:(size//2)])
                two.append(paper[i][(size//2):])
            else:
                three.append(paper[i][0:(size//2)])
                four.append(paper[i][(size//2):])
        sol(one)
        sol(two)
        sol(three)
        sol(four)

n = int(sys.stdin.readline())
if n not in limit:
    print("range error")
    sys.exit()

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sol(paper)
print(white)
print(blue)