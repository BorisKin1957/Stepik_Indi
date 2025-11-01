numbers = list(map(int, input().split()))
flag = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        flag = False
        break

print(flag)
