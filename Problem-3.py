
a = int(input("Enter the Number:"))

if a%2==0:
    a=a-1

num =1

for i in range(a):
    print(num, end=",")
     
    num = num + 2