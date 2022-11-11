listOfRows = []
rows=largestProduct=c=r=0

with open('TriangleOfNums.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
        rows+=1
    
for i in range(0, len(listOfRows)):
    row = listOfRows[i].split("\n")
    listOfRows[i] = row[0].split()

#brute force
for i in range(0, 1000000):
    for r in range(0, 15):
        #do stuff
    