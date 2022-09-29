# a = int(input("enter range start point:"))
# b = int(input("enter range end point:"))
# for i in range(a, b+1):
#     if i > 1:
#         for j in range(2,i):
#             if (i%j) == 0:
#                 break
#         else:
#             print(i)


# def prime(a, b):
#     count = 0
#     next = 2
#     while a <= b:
#         while next >= b:
#             # if a
#             print(a,b)


# prime(1, 20)

def prime(a, b):
    # num = 1
    while a <= b:
        count = 0
        next = 2
        
        while next <= a//2:
            if a % next == 0:
                count += 1
                break
            next += 1
        if count == 0 and a != 1:
            print(a)
        a += 1
        return 


x = int(input("enter start point:"))
y = int(input("enter end point:"))
prime(x, y)
print(prime(x, y))
