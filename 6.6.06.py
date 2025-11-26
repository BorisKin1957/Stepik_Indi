result = {}

n = int(input())
for _ in range(n):
    word = input().split()
    if len(word) > 1:
        result[word[0]] = ' '.join(word[1:])
    else:
        result[word[0]] = None

print(result)