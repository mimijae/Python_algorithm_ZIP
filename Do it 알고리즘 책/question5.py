# 나머지 합 구하기 
# (A + B) % C 는 ((A % C) + (B % C)) % C 와 같다
# 구간 합 배열을 이용한 식 S[j]-S[i] 는 원본 리스트의 i+1 부터 j까지의 구간 합이다.
# 구간 합 배열의 원소를 M으로 나눈 나머지로 업데이트하고 S[j] S[i]가 같은 (i,j)쌍을 찾으면 원본 리스트에서 i+1 부터 j 까지의 구간합이 M 으로 나누어 떨어진다는 것을 알수있다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A=list(map(int, input().split()))
S=[0]*n
C=[0]*m
S[0]=A[0]
answer=0

for i in range(1,n):
    S[i]=S[i-1]+A[i]

for i in range(n):
    remainder=S[i]%m
    if remainder==0:
        answer+=1
    C[remainder]+=1

for i in range(m):
    if C[i]>1:
        answer+=(C[i]*(C[i]-1)//2)

print(answer)

