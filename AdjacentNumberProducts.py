
listOfRows = []
rows=largestProduct=c=r=0
columns = 20
with open('NumberGrid.txt', 'r') as reader:
    for line in reader:
        listOfRows.append(line)
        rows+=1
    
for i in range(0, len(listOfRows)):
    row = listOfRows[i].split("\n")
    listOfRows[i] = row[0].split()
    



while True:
    if c >= columns - 3:
        c=0
        r+=1
        if r == rows:
            break
    product = int(listOfRows[r][c]) * int(listOfRows[r][c+1]) * int(listOfRows[r][c+2]) * int(listOfRows[r][c+3]) 
    if product > largestProduct:
        largestProduct = product
    c+=1
c=r=0
while True:
    if r >= rows - 3:
        r=0
        c+=1
        if c == columns:
            break
    product = int(listOfRows[c][r]) * int(listOfRows[c][r+1]) * int(listOfRows[c][r+2]) * int(listOfRows[c][r+3]) 
    if product > largestProduct:
        largestProduct = product
    r+=1
c=r=0
while True:
    if c >= columns - 3:
        c=0
        r+=1
        if r == rows - 3:
            break
    product = int(listOfRows[r][c]) * int(listOfRows[r+1][c+1]) * int(listOfRows[r+1][c+2]) * int(listOfRows[r+1][c+3]) 
    if product > largestProduct:
        largestProduct = product
    c+=1
c=r=0
while True:
    if c >= columns - 3:
        c=0
        r+=1
        if r == rows - 3:
            break
    print(r, c)
    product = int(listOfRows[r][c+3]) * int(listOfRows[r+1][c+2]) * int(listOfRows[r+2][c+1]) * int(listOfRows[r+3][c]) 
    if product > largestProduct:
        largestProduct = product
    c+=1

print(largestProduct)

