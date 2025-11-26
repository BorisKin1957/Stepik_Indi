numbers = list(map(int, input().split()))
result = {}

for number in numbers:
    result.setdefault(number, numbers.count(number))

print(result)