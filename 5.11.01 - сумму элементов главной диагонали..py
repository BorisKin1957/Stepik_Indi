n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

print(sum([matrix[i][i] for i in range(n)]))