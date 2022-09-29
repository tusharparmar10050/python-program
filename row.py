l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
cl = len (l[0])
rl = len (l)
for i in range(0,rl):
    count = 0
    for j in range(0,cl):
        count += l[i][j]
    print(count)