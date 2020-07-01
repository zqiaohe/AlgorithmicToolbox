one = 0
max = 0
amount = int(input())
i = 0
while i < amount:
    x = input()
    if x == '1':
        one +=1
        if one > max:
            max = one
        i+=1
    else:
        one = 0
        i+=1
print(max)

