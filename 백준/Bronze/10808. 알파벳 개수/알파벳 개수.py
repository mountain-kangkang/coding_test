alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s = input()

for alpha in alphabet:
    count = 0
    for bet in s:
        if alpha == bet:
            count += 1
    print(count, end=' ')