

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(5))


a = int(input("enter range start point:"))
b = int(input("enter range end point:"))

for i in range(a, b+1):
    if i>1:
            
        for j in range(2, i):
            if (i % j) == 0:
                # print(i)
                break
            else:
                print(i)
