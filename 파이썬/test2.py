n = int(input())
white_board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
 
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            white_board[i][j] = 1
 
cnt = 0
for i in range(100):
    for j in range(100):
        if white_board[i][j]:
            cnt += 1
 
print(cnt)