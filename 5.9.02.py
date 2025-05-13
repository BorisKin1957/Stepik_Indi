'''найти сумму всех чётных чисел в этом списке и вывести полученное значение.'''

values = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum([num for lst in values for num in lst if num % 2 == 0]))
