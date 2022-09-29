from operator import index


s = "malayalam is south language"
# w = s[::-1]
# if s == s[::-1]:
#     print("pelindrome")

w = s.split(" ")

j = [i[::-1] for i in w]
k = " ".join(j)
print(k)    


t= 111101010010100
s= str(t)
l = []
print(s)
s2 = ""
l = [i for i in s if i !="0"]
print(l)
for i in l:
    s2+= i

print(int(s2))

# for i in s:
#     if i == "0":
#         continue
#     else:
#         print(i)
#         l.append(i)
# print(l)
