listOfRows = []
rows=largestNum=c=r=0

with open('TriangleOfNums2.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
        rows+=1
    
for i in range(0, len(listOfRows)):
    row = listOfRows[i].split("\n")
    listOfRows[i] = row[0].split()

max = [int(listOfRows[0][0])]

for r in range(1, rows):
    newMax = []
    newMax.append(max[0] + int(listOfRows[r][0]))
    for c in range(1, len(max)):
        if max[c] > max[c-1]:
            newMax.append(max[c] + int(listOfRows[r][c]))
        else:
            newMax.append(max[c-1] + int(listOfRows[r][c]))
    newMax.append(max[c] + int(listOfRows[r][c+1]))
    max = newMax
print(newMax)

answer = newMax[0];     
for i in range(1, len(newMax)):        
   if(newMax[i] > answer):    
       answer = newMax[i];    
           
print("Largest route:", answer)
#after looking at other's answers, it seems it would've been easier to start
# at the bottom