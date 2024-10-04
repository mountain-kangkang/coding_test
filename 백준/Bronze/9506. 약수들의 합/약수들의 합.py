while True:
    n = int(input())
    if n == -1:
        break
    temp = []
    for i in range(1, n):
        if n % i == 0:
            temp.append(i)
    if n == sum(temp):
        print(f"{n} = ", end='')
        for j in range(len(temp)):
            print(temp[j], end='')
            if j + 1 == len(temp):
                print()
                break
            print(" + ", end='')
    else:
        print(f"{n} is NOT perfect.")