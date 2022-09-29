


i = 1
num = 65
n = 5
while i <= n:
    j = 1
    while j <= i:
        if j == 1:
            print(" " * (n- i) + chr(65))
        else:
            ch = chr(num)
            x= n - i
          
            print(" "*x + ch)
        j = j+1
    num += 1
    i +=1
    # print()


n = 5
i = 0
ch = chr(65)
while (i <= n):
    print(" " * (n - i) + chr(65)*i)
    i += 1