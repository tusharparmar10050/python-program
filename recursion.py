# def piramid(n):
#     if n<=0:
#         return
#     else: 
#         print("* "*n,end=" ")
#     print()
#     return piramid(n-1)

# piramid(5)

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))



# a=5
# b=10
# c=0

# # c=b
# # b = a
# # a=c
# # c=b
# a = b
# b = c
# c=a
# print(a)
# # print(c)
# print(b)

# x = 10
# y =20
# x=x+y

# y = x - y
# x = x-y
# print(y)
# print(x)


# l = [2,4,5,3,1]
# temp = 0

# for i in l:
#     for j in range(i+1):
#         if j>i:
#             print(i, j)

# list(map(lambda x: x%2 ==0,range(0,10)))
# print(list(map(lambda x: x%5 ==3,range(0,100))))




# --------------------iterators-----------------------------------------------------

s = "hello"
iter1 = iter(s)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))



# -------Generator---------------------------------------------------------------
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)



def make_printer(msg):

    msg = "hi there"

    def printer():
        print(msg)

    return printer


myprinter = make_printer("Hello there")
myprinter()
myprinter()
myprinter()














# ---------------------decorator-----------------------
def star(func):
    def inner(msg):
        print("* " * 30)
        func(msg)
        print("* " * 30)
    return inner


def percent(func):
    def inner(msg):
        print("% " * 30)
        func(msg)
        print("% " * 30)
    return inner

 
@star
@percent
def printer(msg):
    print(msg)


printer("Hello")