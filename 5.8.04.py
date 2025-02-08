'''
Морской бой - 2

«Морской бой» - игра для двух участников, в которой игроки по очереди называют координаты на неизвестной им карте соперника.
 Если у соперника по этим координатам имеется корабль, то корабль или его часть «топится»,
 а попавший получает право сделать еще один ход. Цель игрока - первым поразить все корабли противника.

«Морской бой» очень популярен среди учеников одной физико-математической школы. Ребята очень любят в него
играть на переменах. Вот и сейчас ученики Иннокентий и Емельян начали новую партию.

Правила, по которым ребята расставляют корабли перед началом партии, несколько отличаются от классических.
 Во-первых, игра происходит на поле размером N×M, а не 10×10. Во-вторых, число кораблей, их размер и форма
 выбираются ребятами перед партией - так играть намного интереснее.

Емельян уже расставил все свои корабли, кроме одного однопалубного. Такой корабль занимает ровно одну клетку.

Задана расстановка кораблей Емельяна. Найдите число способов поставить оставшийся однопалубный корабль.
При этом учитывайте, что по правилам его можно ставить только в ту клетку, все соседние с которой не заняты.
В этой задаче соседними считаются клетки, имеющие общую сторону.

Программа считывает два числа: N и M (1 ≤ N, M ≤ 100). Последующие N строк описывают игровое поле -
каждая из них содержит M символов. Символом «.» (точка) обозначена свободная клетка, символом «*» (звездочка) - занятая кораблем.

Необходимо вывести на экран ответ на задачу

Разбор задачи

Sample Input 1:

4 4
****
**..
*...
*...

Sample Output 1:

4

Sample Input 2:

4 3
***
...
...
***

Sample Output 2:

0

Sample Input 3:

2 3
...
...

Sample Output 3:

6

Sample Input 4:

3 5
***..
..**.
...**

Sample Output 4:

3

Верно решили 2 627 учащихся
Из всех попыток 42% верных
Отличное решение! '''

n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]
count = 0

for row in matrix:
    row.insert(0, '.')
    row.append('.')

matrix.insert(0, list('.' * (m + 2)))
matrix.append(list('.' * (m + 2)))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i][j] == '.':
            if matrix[i][j + 1] == '*' or matrix[i + 1][j] == '*' or matrix[i - 1][j] == '*' or matrix[i][j - 1] == '*':
                continue
            else:
                count += 1
print(count)