data=list(map(int,input().split()))
cmp=sorted(data)
cmp_reversed=sorted(data,reverse=True)

if data==cmp:
    print('ascending')
elif data==cmp_reversed:
    print('descending')    
else:
    print('mixed')    