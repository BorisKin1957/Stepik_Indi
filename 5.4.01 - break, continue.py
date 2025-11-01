trans = map(int, input().split())

for value in trans:
    if value <= 0:
        print(value > 0)
        break
else:
    print(value > 0)