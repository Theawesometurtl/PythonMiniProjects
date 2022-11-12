listOfRows = []
rows=largestNum=c=r=0

with open('TriangleOfNums1.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
        rows+=1
    
for i in range(0, len(listOfRows)):
    row = listOfRows[i].split("\n")
    listOfRows[i] = row[0].split()

#brute force
max = [int(listOfRows[0][0])]

for r in range(1, rows):
    newMax = []
    newMax.append(max[0] + int(listOfRows[r][0]))
    for c in range(1, len(max)):
        if max[c] > max[c-1]:
            newMax.append(max[c] + int(listOfRows[r][c]))
        else:
            newMax.append(max[c-1] + int(listOfRows[r][c]))
    print(max[c])
    print(listOfRows[r][c+1])
    newMax.append(max[c] + int(listOfRows[r][c+1]))
    max = newMax
    print(newMax)