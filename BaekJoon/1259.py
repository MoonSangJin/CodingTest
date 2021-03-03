data=[]
while True:
    a=input()
    if a=='0':
        break
    else:
        data.append(a)
for i in data:
    j=reversed(i)
    if list(i)==list(j):
        print('yes')
    else:
        print('no')    




    