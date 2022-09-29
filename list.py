# score = int(input("Enter the score:"))


# if score < 100 and score > 70: 
#     print("You are pass With First Class")
# elif score <= 70 and score > 50:
#     print("You are pass With Second class")
# elif score <= 50 and score > 35:
#     print("You are pass")
# else:
#     print("you are fail")



# from itertools import count


# score = int(input("Enter the number:"))


# if score > 0: 
#     print("The number is positive:")
# elif score < 0:
#     print("the number is nagative:")
# else:
#     print("The number is zero")


# # while loop

# n = int(input("enter the number:"))

# count = 10

# while count >=1:
#     t = n*count
#     print(n , "X" , count , "=" , t)
#     count = count - 1
    




# lang = ["python" , "java", "swift", "c", "c++"]

# for val in ["python" , "java", "swift", "c", "c++"]:
#     if val == "swift":
#         continue
#     elif val == "c++":
#         continue
#     print(val)

    

# sum = 0
# for count in range(101):
#     sum += count
    
#     print(sum)

# print(sum)
# for i in reversed(range(101)):
#     print(i)


def add(n1, n2):
    sum = n1 + n2
    return sum
def multi(n1, n2):
    mult = n1*n2
    return mult



number1 = 20
number2 = 10

sum = add(number1,number2)
print("sum is:", sum)

mult = multi(number1,number2)
print("multi is:", mult)

def factorial(x):
    if x==1:
        return 1
    else:
        return (x* factorial(x-1))


num = int(input("enter the number:"))
print("factorial of :",num , "is", factorial(num) )