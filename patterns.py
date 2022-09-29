i = 1
num = 65
while i <= 5:
    j = 1
    while j <= i:
        if j == 1:
            print("A", end='')
        else:
            ch = chr(num)
            print(ch, end='')
        j = j+1
    num += 1
    print()
    i +=1



i = 1
num = 65
while i <= 10:
    j = 1
    while j <= i:
        if j == 1:
            print(chr(65), end='')
        elif j < i:
            print(chr(num+(j-1)), end='')
        else:
            print(chr(65), end='')
        j = j+1
    print()
    i +=1


i = 1

while i <= 5:
    j = 1
    while j <= i:
        if j == 1:
            
            print(1, end='')

        else:
            
            print(j, end='')
        
        j = j+1
    print()
    i +=1


# python3 code to print pyramid pattern using while loop
n = 5
i = 0
while (i <= n):
    print(" " * (n - i) + "*" * i)
    i += 1
