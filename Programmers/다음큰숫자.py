def binary(n):
    binary_number=[]
    while n>0:
        binary_number.append(n%2)
        n=n//2
    binary_number.reverse()
    k=list(map(str,binary_number))
    k=''.join(k)
    return k
        
def solution(n):
    answer = 0
    a=binary(n)
    a_number=a.count('1')
    n+=1
    while True:
        b=binary(n)
        b_number=b.count('1')
        if a_number==b_number:
            answer=n
            break
        else:
            n+=1
            
        
    return answer