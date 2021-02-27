<h1 align="center">📚Coding Test</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Coding_Test를 준비하는 기록 (코테를 가뿐히 통과하는 그날까지)

## Author
👤 **MoonSangJin**
* Github: [@MoonSangJin](https://github.com/MoonSangJin)
* Based On : [@KIMJINOH97](https://github.com/KIMJINOH97/Algorithm) 


# 알고리즘 python method 요약

## Str 관련 Method

<table>
    <th>Method</th>
    <th>Return</th>
    <th>Ex</th>
    <tr>
        <td><b>str.split()</b></td>
        <td>문자열을 기준에 다라 나눠 list로 반환</td>
        <td>
            str = 'I am jinoh' <br>
            str.split() -> ['I', 'am', 'jinoh']<br>
        </td>
    </tr>
    <tr>
        <td><b>'string'.join()</b></td>
        <td>string을 list파라미터의 중간에 넣어 합친 str로 반환</td>
        <td>
            li = ['I', 'am', 'jinoh']
            ' 'join(li) -> 'I am jinoh'<br>
        </td>
    </tr>
    <tr>
        <td><b>str.replace()</b></td>
        <td>문자열의 원하는 부분을 바꾸어 그 string을 반환</td>
        <td>
            str = 'I am jinoh' <br>
            str.replace('jinoh', 'python') -> 'I am python'<br>
        </td>
    </tr>
    <tr>
        <td><b>str.find()</b></td>
        <td>매개변수로 입력한 문자열의 index 반환 없으면 -1</td>
        <td>
            str = 'abba' <br>
            str.find('a') -> 1 반환<br>
            str.find('a', 2) -> 3반환<br>
            </td>
    </tr>
    <tr>
        <td><b>str.startswith()</b></td>
        <td>문자열의 앞에서 부터 찾아 index 반환 없으면 -1</td>
        <td>
        str = 'I am jinoh' <br>
        str.startswith('I') -> True <br>
        str.startswith('I am') -> True
    </td>
    </tr>
    <tr>
        <td><b>str.endswith()</b></td>
        <td>매개변수로 문자열이 끝나면 True, 그렇지 않으면 False</td>
        <td>
            str = 'I am jinoh' <br>
            str.endswith('jinoh') -> True <br>
            str.endswith('joh') -> false <br>
        </td>
    </tr>
    <tr>
        <td><b>str.count()</b></td>
        <td>매개변수의 문자열이 몇개 있는지 반환(대 소문자 구분)</td>
        <td>
            str('문자열', 시작위치, 끝위치) 가능
            str = 'I am jinoh' <br>
            str.count('i') -> 1반환<br>
            str.count('o', 7, len(str)) -> 1반환
    </td>
    </tr>
    <tr>
        <td><b>str.index()</b></td>
        <td>find와 동일하나 없으면 ValueError</td>
        <td>
            str = 'I am jinoh' <br>
            str.index('a') -> 3반환<br>
            str.index('k') -> ValueError
        </td>
    </tr>
    <tr>
        <td><b>str.isalpha()</b></td>
        <td>문자열이 영어,한글로만 이루어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh' <br>
            str2 = '123 I am'<br>
            str1.isalpha() -> True<br>
            str2.isalpha() -> False
        </td>
    </tr>
    <tr>
        <td><b>str.isdigit()</b></td>
        <td>문자열이 숫자로만 이루어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jin5' <br>
            str2 = '123124'<br>
            str1.isdigit() -> False<br>
            str2.isdigit() -> True
        </td>
    </tr>
    <tr>
        <td><b>str.islower()</b></td>
        <td>문자열이 모두 소문자로만 되어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh'<br>
            str2 = 'I AM JINOH'<br>
            str1.isalpha() -> True<br>
            str2.isalpha() -> False
        </td>
    </tr>
    <tr>
        <td><b>str.isupper()</b></td>
        <td>문자열이 모두 대문자로만 되어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh'<br>
            str2 = 'I AM JINOH'<br>
            str1.isupper() -> False<br>
            str2.isupper() -> True
        </td>
    </tr>
    <tr>
        <td><b>str.lower()</b></td>
        <td>문자열을 모두 소문자로 변환</td>
        <td>
            str1 = 'I Am jinoh'<br>
            str1.lower() -> 'i am jinoh' 반환
        </td>
    </tr>
    <tr>
        <td><b>str.upper()</b></td>
        <td>문자열을 모두 대문자로 변환</td>
        <td>
            str1 = 'I am jinoh'<br>
            str1.upper() -> 'I AM JINOH' 반환
        </td>
    </tr>
    <tr>
        <td><b>str[::-1]</b></td>
        <td>문자열을 뒤집는다</td>
        <td>
            str1 = 'hello'<br>
            str1[::-1] -> 'olleh' 반환
        </td>
    </tr>
</table>

## list 관련 Method

<table>
    <th>Method</th>
    <th>Return</th>
    <th>Ex</th>
    <tr>
        <td><b>list.append()</b></td>
        <td>해당 리스트에 매개변수를 맨 뒤에 추가 반환값 X</td>
        <td>
            li = ['I', 'am'] <br>
            li.append('jinoh') -> ['I', 'am', 'jinoh'] <br>
        </td>
    </tr>
    <tr>
        <td><b>list.pop()</b></td>
        <td>해당 리스트에 지정 인덱스를 제거 후 그 수를 반환</td>
        <td>
            li = ['I', 'am', 'kim', 'jinoh']<br>
            li.pop() -> ['I', 'am', 'kim'] default -1번째<br>
            li.pop(1) -> li = ['I', 'kim'] return 'jinoh'
        </td>
    </tr>
    <tr>
        <td><b>list.remove()</b></td>
        <td>해당 리스트에 매개변수를 제거 후 그 수를 반환 없으면 ValueError</td>
        <td>
            li = ['I', 'am', 'jinoh']<br>
            li.remove('I') -> ['am', 'jinoh']<br>
            li.remove('a') -> ValueError
        </td>
    </tr>
    <tr>
        <td><b>list.reverse()</b></td>
        <td>리스트의 객체를 리스트 안에서 반대로 함</td>
        <td>
            li = [1, 2, 3, 4] <br>
            li.reverse() -> [4, 3, 2, 1]
        </td>
    </tr>
    <tr>
        <td><b>list.insert()</b></td>
        <td>해당 리스트의 원하는 위치에 값을 대입한다</td>
        <td>
            li = [1, 2, 3, 4] <br>
            li.insert(0, 5) -> [5, 4, 3, 2, 1]
        </td>
    </tr>
    <tr>
        <td><b>list.sort()</b></td>
        <td>리스트를 순서대로 정렬함</td>
        <td>
            li = [2, 3, 1, 4] <br>
            li.sort() -> [1, 2, 3, 4] default는 오름차순<br>
            li.sort(reverse = True) -> [4, 3, 2, 1]
        </td>
    </tr>
    <tr>
        <td><b>list.count()</b></td>
        <td>매개변수의 문자열이 몇개 있는지 반환(대 소문자 구분)</td>
        <td>
            str('문자열', 시작위치, 끝위치) 가능
            li = ['I', 'am','jinoh'] <br>
            li.count('i') -> 0반환<br>
            li.count('am', 1, len(li)) -> 0반환
    </td>
    </tr>
    <tr>
        <td><b>filter(func, iterable)</b></td>
        <td>iterable에서 func 조건을 만족한 객체 반환</td>
        <td>
            li = [1, 0 , 0, 1, 1] <br>
            li = list(filter(lambda x: x != 0, li))-> [1, 1, 1] 반환<br>
    </td>
    </tr>
    <tr>
        <td><b>sorted(iterable, key=lambda x: x)</b></td>
        <td>조건에 맞는 것을 정렬하여 정렬된 list반환</td>
        <td>
            li = [[0,1], [1,0], [2,2], [-1,3]] <br>
            sorted(li, key=lambda x: x[0]) <br>
            -> [[-1,3], [0,1], [1,0], [2,2]] 반환 <br>
            sorted(li, key=lambda x: x[1]) <br>
            -> [[1,0], [0,1], [2,2], [-1,3]] 반환 <br>
    </td>
    </tr>
    </tr>
    <tr>
        <td><b>list.sort(key)</b></td>
        <td>조건에 맞는 것을 정렬한다 반환값은 None</td>
        <td>
            li = [[0,1], [1,0], [2,2], [-1,3]] <br>
            li.sort(key=lambda x: x[0]) <br>
            -> li = [[-1,3], [0,1], [1,0], [2,2]] 반환 <br>
            li.sort(key=lambda x: x[1]) <br>
            -> li = [[1,0], [0,1], [2,2], [-1,3]] 반환 <br>
    </td>
    </tr>
    <tr>
        <td><b>map(func, iterable)</b></td>
        <td>각 요소들을 해당 조건에 맞게 바꿔 객체를 반환한다. (map object)</td>
        <td>
            li = ['1', '2', '3', '4'] <br>
            map(int, li) <br>
            -> map object를 반환함 <br>
            제대로된 출력을 위해서는 <br>
            li = list(map(int, li)) <br>
            -> li = [1,2,3,4]로 바뀜 <br>
            # 응용을 해보면<br>
            def func(n): return n-1 <br>
            li = map(func, li) <br>
            -> li = [0,1,2,3] 반환
    </td>
    </tr>
</table>

## dictionary

### 불변한 key와 변할 수 있는 value로 맵핑된 순서없는 집합

```
dic = {"jinoh" : 24, "jinwuk" : 27}
// key로 해당 value 접근

dic['jinoh'] // 24 반환

dic['jinsuk'] = 32 // 새로운 키와 값을 추가

dic['jinoh'] = 25 // 키가 중복되면 마지막 값으로 덮여씌워짐
// dic = {'jinoh' : 25, 'jinwuk' : 27, 'jinsuk' : 32 }

for key in dic:
    print(dic[key]) // 키값으로 딕셔너리 순회가능


```

## 정규표현식

<table>
    <th>Method</th>
    <th>Return</th>
    <tr>
        <td><b>p.match(str)</b></td>
        <td>문자열이 조건에 맞는지 판단해 객체를 반환</td>
    </tr>
    <tr>
        <td><b>p.findall(str)</b></td>
        <td>조건에 맞는 문자열을 추출해 리스트로 반환</td>
    </tr>
    <tr>
        <td><b>p.match(str)</b></td>
        <td>문자열이 조건에 맞는지 판단</td>
    </tr>
</table>

```
import re

str = '1a2b3c4d'
p = re.compile('[a-zA-Z]')
// 위 코드의 축약 result = re.match('[a-z]+', "1a2b3c4d")

p.findall(str) // ['a', 'b', 'c', 'd'] 일치된 문자 없으면 [] 반환
p.match(str) // 'None'

all = re.compile('[a-zA-Z]+')
result = all.match(str)

print(result.group()) // '1a2b3c4d' result가 None이 아니어야 함.



```

## set (집합)

<table>
    <th>Method</th>
    <th>Return</th>
    <tr>
        <td><b>a & b</b></td>
        <td>두 집합의 교집합을 반환</td>
    </tr>
    <tr>
        <td><b>a | b</b></td>
        <td>두 집합의 합집합을 반환</td>
    </tr>
</table>

```
a = [1, 1, 2, 2, 3, 4]
b = [3, 4, 5, 6]

a = set(a) // a = {1, 2, 3, 4}
b = set(b) // b = {3, 4, 5, 6}

c = a & b // c = {3, 4}
c = a | b // c = {1, 2, 3, 4, 5, 6}


```

## Number
```
a = float(input())  //실수입력
b = round(a, 2) //소수점 3번째에서 반올림처리해서 2번째까지만 나타내기
print('%.2f' % b) //소수점 둘째자리까지만 나타내기

```

## Input
```
input()은 입력받은걸 문자열로 나타냄
input().split()은 입력받은 문자열을 공백으로 나눠서 리스트로 만듬
map(int,input().split())은 만들어진 리스트의 모든원소에 int 함수 적용
list(map(int,input().split()))는 모든 원소에 int함수 적용시킨 결과를 다시 리스트로 만듬

y, m, d = map(int, input().split('.'))  //.으로 나눠진걸 int로 만들고
print('%d.%02d.%02d' % (y, m, d)) // 문자열형식으로 나타낼건데 들어갈 변수는 따로 %로 넣는다 %02

a,b=input().split('.') //.을 기준으로 문자열 두개를 받는데
print(a+b) 하면 붙여서 문자열로나오는데
print(a,b) 하면 a나오고 한 칸 띄고(스페이스) b가 나온다



```
Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

```

```
