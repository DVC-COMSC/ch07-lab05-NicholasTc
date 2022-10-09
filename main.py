
# ******************************
# Make your Code
# ******************************
strval = input().split()
numbers = []

for n in strval:
    numbers.append(int(n))

num = int(input())
reoccur = numbers.count(num)

print(reoccur)

# the below llin 11 are same as the lines from 5 to 8
# numbers = list(map(int, strval))
# print (numbers)
