n=input()
middle=len(n)//2
left=0
right=0
for i in range(middle):
    left+=int(n[i])
for j in range(middle,len(n)):
    right+=int(n[j])
if left==right:
    print('LUCKY')
else:
    print('READY')    
