# a=1
# try:
#     if a==0:
#         b=a/0
#         print(b)
#     else:
#         print("not sem")
# except Exception as e:
#     print(e)
# finally:
#     print("error")

a =[1,2,3,4,5,6,7,8,9,10]

itr = iter(a)


def ge(a):
    for itr in a:
        yield itr*1000
    

b = ge(a)
print(b)
print(next(b))
        

from datetime import datetime

def start(func):
    def st():
        start_time = datetime.now()
        print("* " * 30)
        print("Start time : ",start_time)
        func()
        end_time = datetime.now()
        print("End time : ",end_time)
        print("* " * 30)
        print("Execution time : ", end_time-start_time)
    return st

@start
def calc():
    k = []
    for i in range(500):
        k.append(i)
    return k

calc()
