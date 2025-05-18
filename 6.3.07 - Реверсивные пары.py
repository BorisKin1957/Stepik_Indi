'''Вы работаете над системой текстовой обработки и анализируете список строк. Ваша задача — для каждой строки создать пару, состоящую из самой строки и её перевёрнутой версии. Если строка является палиндромом (читается одинаково в обе стороны), добавьте в итоговый список только эту строку, без пары.

Напишите программу, которая:

обрабатывает список строк strings;

Для каждой строки создаёт кортеж из пары значений, состоящую из самой строки и
её перевёрнутой версии;

Если строка является палиндромом, добавляет в список только эту строку.

Выводит итоговый список.
Переменная strings будет объявлена во входных данных, вам вводить ничего не требуется.

Sample Input 1:

strings = ["hello", "world", "madam", "python"]
Sample Output 1:

[('hello', 'olleh'), ('world', 'dlrow'), 'madam', ('python', 'nohtyp')]'''


strings = ["hello", "world", "madam", "python"]

# result = []
#
# for string in strings:
#     if string == string[::-1]:
#         result.append(string)
#     else:
#         result.append((string, string[::-1]))
#
# print(result)

result = [string if string == string[::-1] else (string, string[::-1]) for string in strings]
print(result)