n=int(input("Enter a number:"))
steps=0
while n>1:
    if n%2==0:
        n=n//2
        print(n)
        steps+=1
        continue
    else:
        n=(n*3)+1
        print(n)
        steps+=1
        continue
else:
    print("steps="+str(steps))