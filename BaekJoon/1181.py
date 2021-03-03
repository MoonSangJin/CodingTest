n=int(input())
data_list=[]
for _ in range(n):
    data=input()
    data_len=len(data)
    data_list.append((data,data_len))
data_list=list(set(data_list))
answer=sorted(data_list,key=lambda x:(x[1],x[0]))
for i in answer:
    print(i[0])
