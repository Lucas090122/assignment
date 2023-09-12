import random
n = int(input("how many dice to roll?\n"))
a = 0
lst = []
while a < n:
   i = random.randint(1, 6)
   lst.append(i)
   a+=1
sum = 0
for num in lst:
   sum+=num
print(sum)