a=int(input("a:"))
b=int(input("b:"))
count1=0
count2=0
for i in range(a,b+1):
    if(i%2==0):
        count1=count1+1
    else:
        count2=count2+1

print("odd number count=",count2)
print("even number count=",count1)