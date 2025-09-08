a=int(input("Enter the number: "))
s=0
while(a>0):
    r=a%10
    a=a//10
    s=s+r
print("The sum is {}".format(s))