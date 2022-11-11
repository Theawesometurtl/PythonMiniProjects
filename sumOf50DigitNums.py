listOfRows = []
sum=0
with open('50digitNums.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
    
for i in range(0, 100):
    row = int(listOfRows[i].split("\n")[0])
    sum+=row
    
print(sum)