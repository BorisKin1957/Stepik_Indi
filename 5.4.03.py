numbers = list(map(int, input().split()))
n = int(input())

for i in range(len(numbers)):
    if n == numbers[i]:
        print(i + 1)
        break
else:
    print('ErrorValue')