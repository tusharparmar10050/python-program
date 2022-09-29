

# s = "Evil olive"
# s = s.lower()
# s1 = s.lower()[::-1]
# print(s1, s)
# if s1.replace(" ", "") == s.replace(" ", ""):
#     print(s1)


# ------------------n natural numbers sum
# def sum(n):
#     if n < 1:
#         return 0

#     else:

#         return n + sum(n-1)


# sum(10)
# print(sum(10))


# ----------------pow------------------------

# def numsum(a, n):
#     if a < 1 or n < 1:
#         return n

#     else:
#         print(pow(a,n))
#         # return numsum(pow(a, n))


# x = int(input("num:"))
# y = int(input("time:"))
# numsum(x, y)
# print(numsum(x, y))

# -----------------------GCD---------------------
# def gdc(o,p):
#     if p==0:
#         return o
#     else:
#         return gdc(p,o%p)

# x = int(input("first Number :"))
# y = int(input("Second Number :"))
# gdc(x, y)
# print(gdc(x,y))


# x = int(input("first Number :"))
# y = int(input("Second Number :"))
# # i = 1
# # while(i<=x and i<=y):
# #     if(x%i==0 and y%i==0):
# #         gcd = i
# #     i+=1

# # print("GCD is: " , gcd)

# if x > y:
#     for i in range(1,x+1):
#         if x % i == 0 and y % i == 0:
#             g = i
#     # print(x)
# else:
#     for i in range(1,y+1):
#         if x % i == 0 and y % i == 0:
#             g = i
#     # print(y)
# print(g)



def fibo(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        return fibo(n - 1)+ fibo(n - 2)

n = int(input("enter the number"))
    for i in range(1, n):
        print(fibo(i))