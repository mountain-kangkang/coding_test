import sys
input = sys.stdin.readline

def solve(star, n):
    in_star = []
    if ((n//3) % 3) == 0:
        for i in range(3):
            if i != 1:
                for s in star:
                    in_star.append(s*3)
            else:
                for s in star:
                    in_star.append(s + ([" "]*len(s)) + s)
        solve(in_star, n//3)
    else:
        for i in star:
            print(''.join(i))

def main():
    star = [
        ["*", "*", "*"],
        ["*", " ", "*"],
        ["*", "*", "*"]
         ]

    n = int(input())

    solve(star, n)

if __name__ == '__main__':
    main()