# dict1 = {'이름': '한사람', '나이': 33}
# data = enumerate(dict1)
# for i, key in data:
#     print(i, ":", key, '->', dict1[key])
# print()
data=list(map(lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),['12','121']))
print(data)