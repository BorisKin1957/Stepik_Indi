messages = ["Заказ отправлен", "Ожидается доставка", "Товар в пути"]
substring = "доставка"

for message in messages:
    if substring.lower() in message.lower():
        print(message)
        break
else:
    print('Подстрока не найдена')