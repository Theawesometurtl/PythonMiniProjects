listOfRows = []
rows=largestNum=c=r=0

with open('TriangleOfNums.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
        rows+=1
    
for i in range(0, len(listOfRows)):
    row = listOfRows[i].split("\n")
    listOfRows[i] = row[0].split()

#brute force
max = [listOfRows[0][0]]
for i in range(0, 1000000):
    for r in range(1, len(listOfRows[i])):
        if max[r] > max[r-1]:
            newMax = max[r]
        else:
            newMax = max[r-1]
    