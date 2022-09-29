# take input
s = int(input("Enter the size of the pattern: "))
# declare 2D array
pattern = [[0 for i in range(s)] for j in range(s)]
print(pattern)
# initialize
num = 1 # starting number
i = 0 # 2d array row index
j = 0 # 2d array column index
m = 0 # to store row index lower limit
n = s - 1 # to store row index upper limit
p = 0 # to store column index lower limit
q = s - 1 # to store column index upper limit
# fill the array to create patern.
# stop when n > s * s
while num <= s * s:
    # fill horizontally left to right
    for j in range(p, q + 1):
        pattern[m][j] = num
        num = num + 1
    # update row index lower limit
    m = m + 1
    # fill vertically top to bottom
    for i in range(m, n + 1):
        pattern[i][q] = num
        num = num + 1
    # update column index upper limit
    q = q - 1
    # fill horizontally right to left
    for j in range(q, p - 1, -1):
        pattern[n][j] = num
        num = num + 1
    # update row index upper limit
    n = n - 1
    # fill vertically bottom to top
    for i in range(n, m - 1, -1):
        pattern[i][p] = num
        num = num + 1
    # update column index lower limit
    p = p + 1
# new line
print("");
# display the pattern
for i in range(0, s):
    for j in range(0, s):
        # print value
        print(pattern[i][j], end = "\t")
    # new line
    print("")