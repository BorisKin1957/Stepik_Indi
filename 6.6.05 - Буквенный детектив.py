word = list(input())

result = {}

for symbol in word:
    result.setdefault(symbol, []).append(word.index(symbol))
    word[word.index(symbol)] = '^'

print(result)