# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if  j == 0:
#             print("1", end="")
#         else:
#             print(j, end="")
#     print('\r') 
         


# # function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]


# # Driver code
# s = str(input("enter string to check:"))
# print("Reverse Of String Is:",s[::-1])
# ans = isPalindrome(s)
# # print(s)
# if ans:
# 	print("String Is Palindrome Yes")
# else:
# 	print("String Is Palindrome No")












from turtle import distance


x = str(input("enter string to check:"))

w = x[::-1]

print(w)
if (x == w):
	print("Yes")
else:
	print("No")




fee = 4535

discount_in_fee = (10/100)*fee

discounted_fee = fee - discount_in_fee

print("total fees are with discount is ", discounted_fee)



distance_km = 4535

mile = 0.621371


distance_mile = distance_km * mile
mile_des = float(distance_mile)
print("total fees are with discount is", distance_mile)
