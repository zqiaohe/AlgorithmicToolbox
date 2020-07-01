input()
numbers = sorted(list(map(int,input().split())), reverse=True)
print(numbers[0]*numbers[1])