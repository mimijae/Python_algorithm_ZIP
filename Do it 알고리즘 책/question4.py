# 구간합 구하기 2
# 2차원 배열 D[i][j]의 값을 채우는 구간 합 공식 아래 공식을 통해 2차원 배열에 값을 채워놓는다 
# D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 질의 X1, Y1, X2, Y2에 대한 답을 구간 합으로 구하는 방법
# D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + D[X1-1][Y1-1]

import sys
input = sys.stdin.readline

n, m=map(int, input().split())

A=[[0]*(n+1)]
D=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)


