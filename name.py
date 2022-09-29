n=7
for i in range(n):
    for j in range(n):
        if i == 0 or j==n//2:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if (((j==1 or j==5) and i!=6 )or(i==6 and j>1 and j<5)):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if (((i==0 or i==3 or i==6)and j>1 and j<5)or (j==1 and (i ==1 or i==2 or i==6))or (j==5 and (i==0 or i == 4 or i==5)) ):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if ((j==1 or j==5)or (i ==3 and (j==2 or j==4 or j==3))):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if ((i==0 and (j==3))or (i==1 and (j==2 or j==4))or(i==2 and (j==1 or j==5))or(i==3 and (j==1 or j==5 or j==1 or j==2 or j==3 or j==4 or j==5))or (i>3 and (j==1 or j==5))):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    for j in range(n):
        if ((i==0 and (j==2 or j==3 or j==4))or (i == 3 and (j==1 or j==2 or j==3 or j==4 or j==5))or(i<3 and(j==1 or j==5))or (i==4 and(j==1 or j==2))or (i==5 and(j==1 or j==3))or (i==6 and(j==1 or j==4))):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
