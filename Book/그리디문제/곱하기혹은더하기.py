data=input()

result=int(data[0])
for i in range(1,len(data)):
    num=int(data[i])
    if result<=1 or num<=1:
        result+=num
    else:
        result*=num
print(result)            

#조건
#처음 숫자 가 1이하면 그다음 수를 더하는게 이득
#그다음 수가 1이하면 결과에 더하는게 이득
#그다음 수가 2이상이면 곱하는게 이득