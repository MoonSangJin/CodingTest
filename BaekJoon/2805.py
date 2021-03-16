#이분탐색
n,m=map(int,input().split())
tree=list(map(int,input().split()))
tree.sort()
temp=[]
#10 15 17 20
def binary(tree,target,start,end):
    global temp
    if start>end:
        return True 
    mid=(start+end)//2

    sum_diff=0
    for i in tree:
        if i>mid:
            sum_diff+=(i-mid)

    if sum_diff>=target:
        temp.append(mid)
        binary(tree,target,mid+1,end)
    elif sum_diff<target:
        binary(tree,target,start,mid-1)
    return True

binary(tree,m,0,1000000000)
print(max(temp))            

