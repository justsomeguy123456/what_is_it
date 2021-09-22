import random

n = random.randint(0,1)

if n == 0:
    l = ['its','a','baby','girl','boy',' ']
else:
    l = ['its','a','baby','boy','girl',' ']


l = ['its','a','baby','girl','boy',' ']


x = 0
answer = ''
while (x)  < len(l):
    answer = answer + l[x]+l[5]

    if (x > 0) and ( x % 2 == 0):
        x = len(l)
    x +=1

print(answer)
