
n = 5
a = 65
num = 0

for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(" ", end="")

    for k in range(0, i * 2 - 1):
        print(chr(a + num), end="")
        num += 1
    num = 0
    print()
for i in range(1, n):
    for j in range(0, i+1):
        print(" ", end="")
    for k in range((n - i) * 2 - 1):
        print(chr(a + num), end="")
        num += 1
    num = 0
    print()


# n = 5
# a = 65
# num = 0

# for i in range(1, n + 1):
#     for j in range(n, i - 1, -1):
#         print(chr(a + num), end="")
#         # print(chr(a + num)+" ", end="")

#         num += 1

#     for k in range(0, i * 2 - 1):
#         print(" ", end="")
#     num = 0
#     print()

# for i in range(1, n):
#     for j in range(0, i+1):
#         print(chr(a + num), end="")
#         num += 1
#     for k in range((n - i) * 2 - 1):
#         print(" ", end="")
#     num = 0
#     print()




# ABCDEFFEDCBA
# ABCDE  EDCBA
# ABCD    DCBA
# ABC      CBA
# AB        BA
# A          A
# AB        BA
# ABC      CBA
# ABCD    DCBA
# ABCDE  EDCBA
# ABCDEFFEDCBA
n = 6

for i in range(n, 0, -1):

    for j in range(i, 0, -1):
        print(chr(65+i-j), end="")
    for j in range(2*(n-i)):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(chr(64+j), end="")

    print()

for i in range(n-1):

    for j in range(i+2):
        print(chr(65+j), end="")
    for j in range(2*(n-i-2)):
        print(" ", end="")
    for j in range(i+2):
        print(chr(66+i-j), end=''"")
    print()




       
   
n = 5
k = 2 * n - 2     
for i in range(n, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("") 


n = 5

# for i in range(n):
#     print(chr(65)*i, end="")
#     print(" "*(n-i)*2, end="")
#     print(chr(65)*i, end="")

#     print()
for i in range(n,0,-1):      
    
    print(chr(65)*i, end="")
    print(" "*(n-i)*2, end="")
    print(chr(65)*i, end="")
    print(chr(65)*i, end="")
    print(" "*(n-i)*2, end="")
    print(chr(65)*i, end="")
    print(chr(65)*i, end="")
    print(" "*(n-i)*2, end="")
    print(chr(65)*i, end="")

    print()







