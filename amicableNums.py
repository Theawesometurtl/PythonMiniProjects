#find the sum of the divisors of a number
def sum_of_divisors(num):
    sum=1
    for i in range(2, (num//2)+1):
        if num % i == 0:
            sum+=i
    return sum

answer=0
for x in range(1, 10001):
    if sum_of_divisors(sum_of_divisors(x)) == x and sum_of_divisors(x) != x:
        answer+=x
        print(x, answer)
print(answer)