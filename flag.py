# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *

# n = 25
# num = 7
# num1 = 14
# for i in range(n):
#     print("*",end=" ")
#     for j in range(num):
#         if j == i:
#             print("* "*j,end=" ")
#         elif j == i+1:
#             print(" "*(i-n)*2, end="")
#     for j in range(num+1, num1):
#         if j == i:
#             print("* "*(i-num),end=" ")

#     # for
#     print()


# *
# * *
# *   *
# *     *
# *       *
# *         *
# * * * * * * *
# * *
# *   *
# *     *
# *       *
# *         *
# *           *
# * * * * * * * *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *

n = 25
num = 7
num1 = 14
for i in range(1, n+1):
    for j in range(num):
        if j == 0 or (j == i-1 or i == num):
            print("*", end=" ")
        else:
            if i != num and i < 7:
                print(" ", end=" ")

    for j in range(num, num1):
        if (j+1 == i) or (i == num1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
