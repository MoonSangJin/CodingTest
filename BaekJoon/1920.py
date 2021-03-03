n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))
n_list.sort()

def binarySearch(array,target,left,right):
    middle_index=(left+right)//2
    middle=array[middle_index]

    if left>right:  #종료조건 잘 생각하자 재귀니까
        print(0)
        return  0

    if target==middle:
        print(1)
        return 0
    elif middle>target:
        binarySearch(array,target,left,middle_index-1)
    elif middle<target:
        binarySearch(array,target,middle_index+1,right)
          

for i in m_list:
    answer=binarySearch(n_list,i,0,len(n_list)-1)   