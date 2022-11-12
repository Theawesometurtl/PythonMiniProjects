
def IsPalendrome(num):
    backwards = str(num) [::-1]
    if backwards == str(num):
        return True
    return False



amount=0
for i in range(0, 10001):
    num=i
    amount+=1
    for x in range(0, 50):
        num+= int(str(num) [::-1])
        if IsPalendrome(num):
            amount-=1
            print(i, amount, num)
            break
