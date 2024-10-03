while True:
    try:
        a, b = map(int, input().split())        # 여기서 sys.stdin.readline()을 사용하면 KeyboardInterrupt가 발생하며 백준에서는 런타임에러(ValueError)가 발생한다
    except EOFError:
        break
    print(a + b)
        
