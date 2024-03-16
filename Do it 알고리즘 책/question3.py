# 구간합 구하기

# 합배열 공식 
# S[i] = S[i-1] + A[i]

# 구간합 공식 구간 i와 j가 주어지고 i번째 수에서 j번째 수까지의 합을 출력하는 문제이다
# 1차원 배열에서 구간합 구하는 공식
# S[j]-S[i-1]

# input = sys.stdin.readline 구문은 위에서 설명한 sys.stdin.readline의 사용법을 input이라는 이름으로 바꿔서 사용하겠다는 의미입니다. 
# 이렇게 하면 코드 내에서 input() 함수를 호출하는 것처럼 보이지만 실제로는 sys.stdin.readline 기능을 사용하게 됩니다.

import sys
input = sys.stdin.readline

suNo, quizNo = map(int, input().split())
num=list(map(int, input().split()))
prefix_sum=[0]
temp=0

for i in num:
    temp=temp+i
    prefix_sum.append(temp)

for i in range(quizNo):
    h, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[h-1])