# 투 포인터 - 연속된 자연수의 합 구하기

n = int(input())

start_index=1
end_index=1
count=1
sum=1

while n!=end_index:
    if n==sum:
        count+=1
        end_index+=1
        sum+=end_index
    elif sum>n:
        sum-=start_index
        start_index+=1
    else:
        end_index+=1
        sum+=end_index


print(count)