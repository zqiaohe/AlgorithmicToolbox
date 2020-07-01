List = []
amount = int(input())
i = 0
while i < amount:
    x = int(input())
    if len(List) != 0:
        for item in List:
            if x < item:
                print(x, "b")
                List.append(x)
                List.sort()
                print(List)
            elif x > item:
                print(x, "a")
                List.append(x)
                List.sort()
                print(List)
            break
    else:
        print(x, "c")
        List.append(x)


for j in List:
    print(j)