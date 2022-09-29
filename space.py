
# * 
# * *
# *   *
# *     *
# *       *
# *         *
# * * * * * * *

n=7
for i in range(n+1):
    print("*",end=" ")
    for j in range(i):
        if j==i-1:
            print("*", end=" ")
        else:
            if i!=n:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()




n = 25
num = 7
num1 = 14
for i in range(n):
    print("*",end=" ")
    for j in range(num):
        if j==i-1:
            print("*", end=" ")
        else:
            if i!=num:
                print(" ", end=" ")
            else: 
                print("*", end=" ")

    for j in range(num, num1):
         if j == i:
            #  print(j, i)    
             print("* "*(i-num),end=" ")


    print()