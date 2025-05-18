'''Дан список игроков players, где каждый элемент — кортеж из имени игрока и его силы.
К примеру:

players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
Игроки могут сражаться друг с другом, если разница их силы не превышает заданный
параметр max_difference.

Напишите программу, которая выводит все возможные битвы, удовлетворяющие этому условию.

Сами переменные players и max_difference определяются во входных данных.
Вам вводить ничего не нужно.

Sample Input 1:

players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
max_difference = 6
Sample Output 1:

Alice vs Bob
Bob vs Charlie
Charlie vs Dave'''

players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
max_difference = 6

for i in range(len(players)):
    for j in range(i + 1, len(players)):
        if abs(players[i][1] - players[j][1]) <= max_difference:
            print(f'{players[i][0]} vs {players[j][0]}')
