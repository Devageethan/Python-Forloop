a=int(input("a:"))
b=int(input("b:"))
count=0
for i in range(a,b+1):
    if(i%2==1):
        count=count+1
print(count)