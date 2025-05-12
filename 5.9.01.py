values = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
count_all, count_even = 0, 0

for row in values:
    count_all += len(row)
    if len(row) > 1:
        count_even += 1

print(count_all, count_even, sep='\n')