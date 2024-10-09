import sys

ver_1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
ver_2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

def painting_check(chess_plate : list) -> int:
    version_1, version_2 = 0, 0
    for row in range(8):
        for column in range(8):
            color = chess_plate[row][column]
            if (row % 2) == 1:
                if (column % 2) == 1:
                    if color == "W":
                        version_2 += 1
                    elif color == "B":
                        version_1 += 1
                else:
                    if color == "W":
                        version_1 += 1
                    elif color == "B":
                        version_2 += 1
            else:
                if (column % 2) == 1:
                    if color == "W":
                        version_1 += 1
                    elif color == "B":
                        version_2 += 1
                else:
                    if color == "W":
                        version_2 += 1
                    elif color == "B":
                        version_1 += 1
    return version_1 if version_1 < version_2 else version_2


N, M = map(int, sys.stdin.readline().split())
if N < 8 or 50 < N or M < 8 or 50 < M:
    print("big pie error")
    sys.exit()
result = []

temp = []
for _ in range(N):
    paint = sys.stdin.readline().strip()
    if len(paint) != M:
        print("painting error")
        sys.exit()
    temp.append(paint)

for i in range(0, N - 7):
    for j in range(0, M - 7):
        temp_temp = []
        for k in range(8):
            painted = temp[i+k][j:j+8]
            temp_temp.append(painted)
        result.append(painting_check(temp_temp))

print(min(result))