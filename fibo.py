# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)


# n = int(input("enter the number: "))
# for i in range(n):
#     print(fibo(i))


# list = []
# n = 10
# for i in range(n):
#     if i ==0:
#         list.append(0)
#     elif i ==1:
#         list.append(1)
#     else:
#         list1 = int(list[-1]) + int(list[-2])
#         list.append(list1)

# print(list)


# l = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(l)):
#      list1 = int(l[-1]) + int(l[-2])
#      l.append(list1)
# print(l)
# ----------squre-------------
# a = [1,2,3,4,5,6,7,8,9,10]
# b = []
# for i in range(1,len(a)+1):
#     b.append(i**3)

# print(b)

# ----------squreroot-------------
# from math import sqrt
# a = [1, 4,9,16,25,36,49, 64, 81 ,100]
# b = []
# for i in a:
#     # s = int(a[i])
#     b.append(int(sqrt(i)))

# print(b)


# from math import sqrt
# a = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# b = []
# for i in range(1,len(a)):
#     s = a[i]
#     if s // i==i:
#         print("*", end=" ")
#     print(s)
#     b.append(i)

# print(b)


# ------------reverse of digit-----------
# n = 321
# rev = 0

# while n!=0:
#     num = n%10
#     rev = rev*10 + num
#     n //= 10

# print(rev)


# -----------------highest number-----------
# l = [1,3,5,4,10,8,9]
# temp = l[0]
# for i in l:
#     if i > temp:
#         temp =  i
# print(temp)
# # -----------------second highest number------------------
# l = [20,22,24,26,27,45,28,44,30,45,45,44.5,32]
# temp = l[0]
# temp2 = l[0]
# for i in l:
#     if i > temp:
#         temp =  i
#         # temp2 = temp
#     elif i> temp2 and i<temp:
#         temp2 =i

# print("Highest number of elements in the array is:",temp)
# print(temp2)

# --------------------------leap year--------------------------
# year = int(input("enter the year :"))
# if (year % 4 == 0) and (year % 100 != 0):
#     print("this is leap year:", year)
# elif (year % 400 == 0) and (year % 100 == 0):
#     print("this is leap year:", year)
# else:
#     print("this is not leap year:", year)
# ----------------list sorting-------------
# l = [1,5,4,7,15,3,21]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
# print("lowest is:", l[0])
# print("highest is:", l[-1])
# print(l)
# ----------------sum of nested list-------------------------


# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# s = []
# for i in l:
#     t = sum(i)
#     s.append([t])


# print(s)
# print(max(s))
# # l = [1,2,3]  ----------use for sum of list----------------
# # count = 0
# # for i in l:
# #     # print(i)
# #     count += i
# # print(count)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
cl = len (l[0])
rl = len (l)
s=[]
for i in range(0,rl):
    count = 0
    for j in range(0,cl):
        count += l[i][j]
    print(count)
    s.append([count])
print(s)
temp = s[0]
for i in s:                               #for max values
    if i > temp:
        temp =  i
print("highest number is:", temp)

# ------------duplicate value---------
# l = [1,2,3,4,1,4,5,6,1,8,9]
# s = []
# s1 = []
# for i in l:
#     if i not in s:
#         s.append(i)
#     else:
#         s1.append(i)
# print("duplicate number is :", s1)

# l = [1,2,3,4,1,4,5,4,6,1,8,9]
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] == l[j]:
#             print(l[j])

