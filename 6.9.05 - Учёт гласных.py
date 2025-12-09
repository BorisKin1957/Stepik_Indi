# Определяем строку с гласными буквами русского алфавита
vowel_letters = 'аеёиоуыэюя'
# Преобразуем введённую строку в нижний регистр
letters = input().lower()
# сортируем строку по индексу символов в строке 'аеёиоуыэюя'
sorted_letters = sorted(letters, key=lambda x: vowel_letters.index(x) if x in vowel_letters else 10)

# Создаём словарь: ключ — гласная буква, значение — количество её вхождений в введённой строке
# Учитываются только те буквы, которые есть в vowel_letters
result = {letter: sorted_letters.count(letter) for letter in sorted_letters if letter in vowel_letters}

print(result)
