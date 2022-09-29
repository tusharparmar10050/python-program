# # ---------------------highest number in nested list -------------------------------
l = [[1, 8, 5], [9, 2, 4], [7, 11, 3], [4, 18, 12]]
cl = len(l[0])
rl = len(l)

s=[]
for i in range(4):
    count = 0
    for j in range(0,3):
        if l[i][j] > count:
            count = l[i][j]
    s.append([count])
print(s)


