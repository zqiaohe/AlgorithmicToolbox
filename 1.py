j = list(input())
s = list(input())

result = 0

for ch in s:
    if ch in j:
        result += 1

print(result)