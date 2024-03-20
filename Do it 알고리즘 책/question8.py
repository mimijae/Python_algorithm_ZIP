# 좋은 수 구하기
# 주어진 N개의 수에서 다른 두수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수' 라고 한다. N개의 수중 좋은수가 총 몇개인지 출력하시오.

N=int(input())
Result=0
A=list(map(int,input().split()))
A.sort()

for k in range(N):
    find=A[k]
    i=0
    j=N-1
    while i<j: # 투 포인터 알고리즘
        if A[i]+A[j] == find:
            if i != k and j != k: # 현재 확인하고 있는 '좋은 수' 후보(find에 해당하는 값)가 자기 자신을 제외한 다른 두 수의 합으로 표현될 수 있는지를 검사하기 위한 것
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j]< find:
            i+=1
        else:
            j-=1

print(Result)
    