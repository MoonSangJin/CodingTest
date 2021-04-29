def binary(a):
    binary=[]
    while a>0:
        binary.append(a%2)
        a=a//2
    binary.reverse()
    binary=list(map(str,binary))
    binary=''.join(binary)
    return binary

def delete_zero(b,cnt_zero):
    cnt_zero+=b.count('0')
    b=b.replace('0','')
    b_length=len(b)
    return b_length,cnt_zero
    
def solution(s):
    answer = []
    cnt=0
    cnt_zero=0
    while s!='1': 
        s_length,cnt_zero=delete_zero(s,cnt_zero)
        s=binary(s_length)
        cnt+=1
    answer.append(cnt)
    answer.append(cnt_zero)
    return answer