addBy=0
add=1
sum=1
for i in range(0, 2000):
    
    if i % 4 == 0:
        i=0
        addBy+=2
        print(sum)
    add+=addBy    
    sum+=add
    print(addBy, add, sum)
print(sum)