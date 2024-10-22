def sol():
    a=[None]*20001
    b=map(int,open(0))          # open() 내장함수는 파일을 읽는 함수인데 매개변수로 숫자 '0'을 입력받으면 터미널로 입력하는 내용이르 읽을 파일로 간주함
    next(b)                     # 처음에 입력한 입력받을 수의 개수를 스킵한듯. 수를 지정해서 반복문을 돌리는것보단 [None]으로 가득찬 배열을 읽는게 더 빠른가 봄
    for i in b:                 # b에 입력되어있는 값을 인덱스로 a[i] 위치에 1 삽입
        if a[i]:
            a[i] += 1
            continue
        a[i]=1
    for i in range(-10000,10001,1):
        if a[i] and a[i] > 1:
            for _ in range(a[i]):
                print(i)
            continue
        elif a[i]:
            print(i)

sol()