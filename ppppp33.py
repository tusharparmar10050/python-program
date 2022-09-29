# i = 1
# n = 5
# while i <= n:
#     j = 1
#     while j <= i:
#         if j == 1:

#             print(1, end='')

#         else:

#             print(j, end='')

#         j = j+1
#     print()
#     i +=1


# n = 5
# i = 1

# while (i <= n):
#     print(" " * (n - i) + i)
#     i += 1


# n= 5
# num =65
# for i in range(n,0,-1):
#     num+=1
#     for j in range(1,i+1):
#         if j == 1:
#             print("A", end='')
#         else:
#             # print(j)
#             ch = chr(num + (j-2) )

#             print(ch, end='')

#         # j+=1
#     print("\r")


# n= 6
# num =65
# for i in range(n,0,-1):
#     num+=1
#     for j in range(1,i+1):
#         if i == 6 or j == 1:
#             print("A", end='')
#         elif j< i:
#             # print(j)
#             ch = chr(num + (j-3) )

#             print(chr(65+j-1), end='')
#         else:
#             print("A", end='')


#     print("\r")


# A
# AB
# ABC
# ABCD
# ABCDE
# ABCD
# ABC
# AB
# A
# n= 5
# num =65
# for i in range(n):
#     num+=1
#     for j in range(1, i+1):
#         ch = chr(num + (j-1) )
#         print(chr(64+j), end='')
#     print("\r")
# for i in range(n,0,-1):
#     num+=1
#     for j in range(1,i+1):
#         print(chr(65+j-1), end='')
#     print("\r")





#      A
#     BA
#    CBA
#   DCBA
#  EDCBA
# FEDCBA
#  EDCBA
#   DCBA
#    CBA
#     BA
#      A
# n = 6
# num = 1

# for i in range(1, n):
#     for j in range(n, 0, -1):
#         if j > i:
#             print(" ", end='')
#         else:

#             ch = chr(num)
#             print(chr(65+j-1), end='')
#     print("\r")
# for i in range(n, 0, -1):
#     for j in range(n, 0  , -1):
#         if j > i:
#             print(" ", end='')
#         else:
#             ch = chr(num)
#             print(chr(65+j-1), end='')
#     print("\r")



n = 6
num = 1



for i in range(n):
    for j in range(1, i+1):
        ch = chr(num + (j-1) )
        print(chr(64+j), end='')
    print("\r")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(65+j-1), end='')
    print("\r")
for i in range(1, n):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end='')
        else:
            print(chr(65+j-1), end='')
    print("\r")

for i in range(n, 0, -1):
    for j in range(n, 0  , -1):
        if j > i:
            print(" ", end='')
        else:
            print(chr(65+j), end='')
    print("\r")



