# 파이썬 코딩 테스트 준비 😎

## 1. 리스트 관련 메서드

| 메서드명 | 사용법 | 설명 | 시간 복잡도 |
| --- | --- | --- | --- |
|append()|변수명.append()|리스트에 원소를 하나 삽입할 때 사용.| O(1)|
|sort()|변수명.sort()|기본 정렬 기능으로 오름차순으로 정렬한다.| O(NlogN)|
|sort()|변수명.sort(reverse = True)|내림차순으로 정렬한다.|O(NlogN)|
|reverse()|변수명.reverse()|리스트의 원소의 순서를 모두 뒤집어 놓는다.|O(N)|
| insert() | insert(삽입할 위치, 삽입할 값) | 특정한 인덱스 위치에 원소를 삽입할 때 사용한다. | O(N) |
| count() | 변수명.count(특정 값) | 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다. | O(N) |
| remove() | 변수명.remove(특정 값) | 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개면 하나만 제거한다. | O(N) |

- insert(), remove() 함수는 시간 복잡도가 O(N)
- 중간에 원소를 삽입한 뒤에, 리스트의 원소 위치를 조정해줘야 하기 때문
- insert() 함수 남발하면 '시간 초과'로 테스트를 통과하지 못할 수도 있다.

- 특정한 원소를 모두 제거하려면? > 파이썬은 이러한 함수를 기본적으로 제공해주지 않음

```python
  a = [1, 2, 3, 4, 5, 5, 5]
  remove_set = {3,5}  # 집합은 { } 로 표현  
  
  # remove_set에 포함되지 않은 값만을 저장
  
  result = [i for i in a if i not in remove_set] # not in 연산자 : 집합에 없으면 True
  print(result)
```

## 2. 문자열 자료형

- 문자열 변수를 초기화활 때는 큰따옴표("")나 작은 따옴표(')를 이용
- 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있다. 그 반대도 가능
- 혹은 백슬래시(\)를 사용하면 Escape 문자열로 표현가능

  ```
  data = 'Hello World'
  print(data)
  
  data = "Don't you know \"Python\"?"
  print(data)
  ```
  
 - 문자열 연결 = '+'
 - 파이썬의 문자열은 내부적으로 리스트와 같이 처리된다.
 - 문자열은 여러 개의 문자가 합쳐진 리스트

   ```
   a = "ABCDEF"
    
   print(a[2 : 4 ])  # CD 출력
   ``` 

## 3. 튜플 자료형
- 파이썬의 튜플 자료형은 리스트와 거의 비슷한데 다음과 같은 차이가 있다.
  - 튜플은 한 번 선언된 값을 변경할 수 없다.
  - 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.

- 예를 들어 하나의 튜플 데이터를 선언한 다음, 값을 출력하고 튜플의 특정한 값을 변경해보자.

  ```
  a = (1, 2, 3, 4) # 튜플 자료형
  print(a) # (1, 2, 3, 4)
  
  a[2] = 7 # 에러 발생
  ```
  
- 튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용.
- 예를 들어 다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에서는 우선순위 큐를 이용하는데,
  해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변경되지 않는다. 그래서 그 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다.
- 알고리즘을 구현하는 과정에서 일부러 튜플을 이용하게 되면 혹여나 자신이 알고리즘을 잘못 작성함으로써 변경하면 안 되는 값의 변경을 예방할 수 있다.
- 또한, 튜플은 리스트에 비해 상대적으로 공간 효율적이고, 일반적으로 각 원소의 성질이 서로 다를 때 주로 사용한다.
- 흔히 다익스트라 최단 경로 알고리즘에서는 '비용'과 '노드 번호'라는 서로 다른 성질의 데이터를, (비용, 노드 번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례

## 4. 사전 자료형 (= Map 자료형 )

- 사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형
- 리스트나 튜플은 값을 순차적으로 저장한다는 특징이 있다.
- 예를 들어 리스트의 값이 [1,2,3]이라고 한다면, 첫 번째 원소는 a[0]으로 1이라는 값을 가진다.
- 하지만 사전 자료형은 키-값 쌍을 데이터로 가진다는 점에서, 우리가 원하는 변경 불가능한 데이터를 키로 사용할 수 있다.
- 사전 자료형이 사용되는 대표적인 예시는 사전(Dictionary)이다.

- 예를 들어 다음과 같이 키-값 쌍으로 구성되는 데이터를 담아야 한다면 어떻게 할 수 있을까?

| 키(Key) | 값(Value) |
| --- | --- |
| 사과 | Apple | 
| 바나나 | Banana | 
| 코코넛 | Coconut | 

- 키로 한글 단어를 넣고, 값으로 영어 단어를 넣어 '사과'의 영어 단어를 알고 싶다면 '사과'라는 키 값을 가지는 데이터에 바로 접근하면 된다.
- 파이썬의 사전 자료형은 내부적으로 '해시 테이블'을 이용하므로, 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
- 해시 테이블은 키-값 쌍으로 구성된 데이터를 처리함에 있어서 리스트보다 훨씬 빠르게 동작한다.

  ```Python
    data = dict() # 사전 자료형 생성
    
    # data['key'] = value
    data['사과'] = 'Apple'
    data['바나나'] = 'Banana'
    data[코코넛'] = 'Coconut'
    
    print(data)  # {'사과':'Apple', '바나나':'Banana', '코코넛':'Coconut'}
  ```
  
  
- 이러한 사전 자료형은 코딩 테스트에서도 자주 사용될 수 있다. 
- 예를 들어 학생의 번호가 1부터 10,000,000 까지 구성되어 있는 상황에서 최대 10,000명의 학생을 선택했다고 가정
- 이후에 특정한 학생 번호가 주어졌을 때 해당 학생이 선택되었는지를 어떻게 빠르게 알 수 있을까?
- 만약 리스트를 이용한다면, 1부터 10,000,000 까지의 각 번호가 '선택 되었는지를 저장할 수 있는' 리스트를 만들어아 한다.
- 다시 말해 1,000만 개 데이터를 저장할 수 있는 리스트를 만들어야 하므로 많은 메모리 공간이 낭비된다.
- 이 중 999만 개 가량의 데이터는 쓰이지 않을 것

- 하지만 사전 자료형을 이용하는 경우, 1,000만 개의 데이터를 담을 필요가 없으며 10,000개의 데이터만 사전 자료구조에 들어가므로 훨씬 적은 메모리 공간을 사용
- 사전 자료형에 특정한 원소가 있는지 검사할 때는 '원소 in 사전'의 형태로 사용할 수 있다.
- 이는 리스트나 튜플에 대해서도 사용할 수 있는 문법

  ```Python
    data = dict()
    data['사과'] = 'Apple'
    data['바나나'] = 'Banana'
    data['코코넛'] = 'Coconut'
    
    # 사전 자료형에서 특정 원소가 있는지 검사
    if '사과' in data :
      print("'사과'"를 키로 가지는 데이터가 존재합니다.")
  ```
  
- 파이썬에서 리스트, 문자열, 튜플 등 **순차적인 정보를 담는 자료형을 iterable 자료형이라고 한다.**
- in 문법은 이러한 iterable 자료형에 모두 사용이 가능하다.
  
  
  
## 사전 자료형 관련 함수
- 키와 값을 별도로 뽑아내기 위한 함수가 있다.
- 키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용하며, 값 데이터만을 뽑아서 리스트로 이용할 때는 values() 함수를 이용한다.
  
  
    ```Python
      data = dict()
      data['사과'] = 'Apple'
      data['바나나'] = 'Banana'
      data['코코넛'] = 'Coconut'
      
      # 키 데이터만 담은 리스트
      key_list = data.keys()
      # 값 데이터만 담은 리스트
      value_list = data.values()
      
      print(key_list)  # dict_keys(['사과', '바나나', '코코넛'])
      print(value_list)  # dict_values(['Apple', 'Banana', 'Coconut'])
    ```


## 5. 집합 자료형

- 파이썬에서는 집합을 처리하기 위한 집합 자료형을 제공한다.
- 집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 집합은 다음과 같은 특징이 있다.
  - 중복을 허용하지 않는다.
  - 순서가 없다.

- 기존에 다루었던 리스트나 튜플은 순서가 있기 때문에, 인덱싱을 통한 자료형의 값을 얻을 수 있었다.
- 반면에 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다.
- 더불어, 집합 자료형에서는 키가 존재하지 않고, 값 데이터만을 담게 된다.
- 특정 원소가 존재하는지 검사하는 연산의 시간 복잡도는 사전 자료형과 마찬가지로 O(1) 이다.

- 사전 자료형에 대해서 다룰 때 언급했던 '학생 번호가 주어졌을 때 해당 학생이 선택되었는지 여부를 출력하는 문제'에서도 집합 자료형이 효과적으로 사용 될 수 있다.
- '특정한 데이터가 이미 등장한 적이 있는지 여부'를 체크할 때 매우 효과적이다.
- 집합 자료형을 초기화할 때는 set() 함수를 이용하거나, 중괄호({}) 안에 각 원소를 콤마(,)를 기준으로 구분해서 넣으면 된다


  ```python
  # 집합 자료형 초기화 방법 1
  data = set([1, 1, 2, 3, 4, 4, 5])
  print(data)
  
  # 집합 자료형 초기화 방법 2
  data = {1, 1, 2, 3, 4, 4, 5}
  print(data)
  ```

## 집합 자료형의 연산
- 기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산이 있다.
- 파이썬은 이러한 집합 자료형의 연산에 대해서 다루고 있다.
- 집합 자료형 데이터 사이에서 합집합을 계산할 때는 '|'를 이용한다.
- 또한 교집합은 '&', 차집합은 '-'를 이용한다.

  ```python
  a = set([1, 2, 3, 4, 5])
  b = set([3, 4, 5, 6, 7])
  
  print(a | b) # {1, 2, 3, 4, 5, 6, 7}
  print(a & b) # {3, 4, 5}
  print(a - b) # {1, 2}
  
  
## 집합 자료형 관련 함수
- 집합 자료형 또한 다른 자료형과 마찬가지로 다양한 함수가 존재한다.
- 하나의 집합 데이터에 값을 추가할 때는 add() 함수
- update() 함수는 여러 개의 값을 한꺼번에 추가하고자 할 때 사용한다.
- 특정한 값을 제거할 때는 remove() 함수를 이용할 수 있다.
- 이때 add(), remove() 함수는 모두 시간 복잡도가 O(1) 이다.


  ```python
  data = set([1, 2, 3])
  print(data) # {1, 2, 3}
  
  # 새로운 원소 추가
  data.add(4)
  print(data) # {1, 2, 3, 4}
   
  # 새로운 원소 여러 개 추가
  data.update([5, 6])
  print(data) # {1, 2, 3, 4, 5, 6}
  
  # 특정한 값을 갖는 원소 삭제
  data.remove(3)
  print(data) # {1, 2, 4, 5, 6}
  ```
  
  
  ## 6. 문법
  
- 여러개의 데이터를 담는 자료형으로 리스트 튜플, 문자열, 사전과 같은 자료형이 존재
- 이 때 자료형 안에 어떠한 값이 존재하는지 확인하는 연산이 필요할 때가 있다.
  
- X in 리스트 : 리스트 안에 X가 들어가 있을 때 참(True)이다.
- X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참(True)이다.

- 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

  ```python
  score = 85
  
  if score >= 80 : result = 'Success'
  else : result = 'Fail'
  ```

- 조건부 표현식을 이용하면 if~else 문을 한 줄에 작성해 사용할 수 있다.

  ```python
  score = 85
  result = 'Success' if score >= 80 else 'Fail'
  ```
  
- 특히 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다.
- 예를 들어 리스트에서 특정한 원소의 값만을 없앤다고 해보자.

  ```python
  
  # 일반적인 코드 작성 방법
  
  a = [1, 2, 3, 4, 5, 5, 5]
  remove_set = {3, 5}
  
  result = []
  for i in a :
    if i not in remove_set :
      result.append(i)

  print(result) # [1, 2, 4]
  
  
  # 간략화한 버전
  
  a = [1, 2, 3, 4, 5, 5, 5]
  remove_set = {3, 5}
  
  result = [i for in a if i not in remove_set ]   # 'a if i not in remove_set' > 조건부 표현식
    
  print(result) # [1, 2, 4]
  
  ```
  
  
- 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
- 예를 들어 "x > 0 and x < 20" 과 "0 < x < 20" 은 같은 결과를 반환.


## 반복문

- while 문 :  조건이 참일 때 한해서, 반복적으로 코드가 수행
- for문 : 리스트를 사용하는 대표적인 for문의 구조는 다음과 같다.
- in 뒤에 오는 데이터에 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문한다.
- in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.


  ```python
    for 변수 in 리스트 :
      실행할 소스코드
  ```
  
- for문에서 수를 차례대로 나열할 때는 range()를 주로 쓰는데, range(시작 값, 끝 값 + 1) 형태로 사용.


  ```python
    result = 0
    
    # i 는 1부터 9까지의 모든 값을 순회
    for i in range(1, 10)
      result += i
  ```
  

- 또한 range()의 값으로 하나의 값만을 넣으면, 자동으로 시작 값은 0이 된다.
- 주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스 부터 방문해야 할 때 이 방법을 사용.
- 반목문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.


## 함수

  ```python
  def 함수명(매개변수) :
    실행할 소스코드
    return 반환 값
    
    
  def add(a, b) :
    return a+b
```    

- 또한 함수를 호출하는 과정에서 인자를 넘겨줄 때, 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다.
- 이 경우 매개변수의 순서가 달라도 상관없다는 점이 특징

```python
  def add(a, b) :
    return a+b
    
  add(b = 3, a = 7)
```

- 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우가 있다.
- 이때는 함수에서 global 키워드를 이용하면 된다.
- global 키워드로 변수를 지정하면, 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.
- 아래 예시에서는 a라는 변수를 함수 안에서도 동일하게 접근하여 값을 변경하고 있다.
- 이를 위해, global 키워드가 사용된 것을 확인할 수 있다.


  ```python
   
   a = 0
   
   def func() :
       global a    # 함수 바깥의 a를 참조
       a += 1
    
   for i in range(10) :
       func()
   
   print(a)
  ```
  
  
- 파이썬에서는 람다 표현식을 사용할 수 있다.
- 람다 표현식을 이용하면 함수를 매우 간단하게 작성하여 적용할 수 있다.
- 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징
- 앞에서 정의했던 add() 함수와 같은 간단한 함수를 정의해야 할 때는 다음처럼 람다 표현식을 효과적으로 사용할 수 있다.


  ```python
    def add(a, b) :
      return a + b
      
    # 일반적인 add() 메서드 사용
    print(add(3,7))    # 10
    
    # 람다 표현식으로 구현한 add() 메서드
    print((lambda a,b : a + b)(3, 7)) # 10
  ```
  
 
  ## 7. 입출력
  
  - 알고리즘 문제 풀이의 첫 번째 단계는 데이터를 입력받는 것이다.
  - 알고리즘 문제의 경우 적절한 입력이 주어졌을 때, 그 입력을 받아서 적절한 알고리즘을 수행한 뒤의 결과를 출력하는 것을 요구
  - 보통 먼저 데이터의 개수가 첫 번째 줄에 주어지고, 처리할 데이터는 그 다음 줄에 주어지는 경우가 많다.


  ```
    입력 예시
    5    # 데이터의 개수
    65 90 75 34 99    # 처리할 데이터
  ```
  
- 파이썬에서 데이터를 입력받을 때는 input()을 이용한다.
- input()의 경우 한 줄의 문자열을 입력 받도록 해준다.
- 만약 파이썬에서 입력받은 데이터를 정수형 데이터로 처리하기 위해서는 문자열을 정수로 바꾸는 int() 함수를 사용해야 한다.
- 그리고 여러개의 데이터를 입력받을 때는 데이터가 공백으로 구분되는 경우가 많다.
- 입력 받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드의 사용 빈도가 매우 높다.
- 이때는 **list(map(int, input().slpit())**  을 이용하면 된다.
    - list(map(int, input().split())의 동작 과정을 알아보자.
    1. 가장 먼저 input()으로 입력 받은 문자열을 split() 이용해 **공백으로 나눈 리스트**로 바꾼 뒤에,
    2. map을 이용하여 해당 리스트의 모든 원소에 int() 함수를 적용한다. # map()은 리스트의 모든 원소에 적용해주는 함수인 듯
    3. 최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장하게 되는 것.
    
    - 이 코드는 정말 많이 사용되므로, 반드시 외우고 있어야 한다.
    - 많은 문제는 공백, 혹은 줄 바꿈을 기준으로 데이터를 구분한다.
    - 파이썬에서는 구분자가 줄 바꿈인지 공백인지에 따라서 다른 처리를 요구한다.
    - 줄바꿈이라면 int(input())을 여러번 사용하면 된다.
    
    
    ```python
    
    > 입력 데이터
    > 5
    > 65 90 75 34 99
     
    
    # 입력을 위한 전형적인 소스코드
    
    # 데이터의 개수 입력
    n = int(input())    # 입력 값을 정수로 받는다.
    # 각 데이터를 공백으로 구분하여 입력
    data = list(map(int, input().split()))
    
    data.sort(reverse = True)
    print(data) # [99, 90, 75, 65, 34]
    
    ```

- 공백으로 구분된 데이터의 개수가 많지 않다면, 단순히 map(int, input().split())을 이용하는 것도 가능.    # 리스트로 만들지 않음
- 예를 들어 문제에서 첫째 줄에 n, m, k가 공백으로 구분되어 입력된다는 내용이 명시되어 있다면, 이 경우에는 다음과 같이 사용 가능

  ```python
  
  > 입력 데이터
  > 3 5 7
  
  # n, m, k를 공백으로 구분하여 입력
  n, m, k = map(int, input().split())    # 입력을 공백으로 분리하여 리스트로 만든 뒤, map으로 모든 원소에 int() 적용
  
  print(n, m, k)    
  
  ```

- 또한 문제를 풀다보면, 입력을 최대한 빠르게 받아야 하는 경우가 있다.
- 흔히 정렬, 이진 탐색, 최단 경로 문제의 경우 매우 많은 수의 데이터가 연속적으로 입력이 되곤 한다.
- 예를 들어 1,000만 개가 넘는 라인이 입력되는 경우, 입력을 받는 것만으로도 시관 초과를 받을 수 있다.
- 그래서 사용하는 언어별로 입력을 더 빠르게 받는 방법을 알고 있어야 한다.
- 파이썬도 마찬가지다. 입력의 개수가 많은 경우에는 단순히 input() 함수를 그대로 사용하지는 않는다.
- 파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문
- 이 경우, 파이썬의 sys 라이브러리에 정의되어 있는 **sys.stdin.readline()** 함수를 이용한다.

  ```python
  
  import sys    # sys 라이브러리 import
  sys.stdin.readline().rstrip()
  ```
  
- sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 **rstrip() 함수를 꼭 호출해야 한다.**  
- readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하러면 rstrip() 함수를 사용해야 한다.
- 이 또한 짧은 코드이니 관행적으로 외워서 사용하자.


  ```python
  
  # readline() 사용 소스코드 예시
  
  > 입력 데이터
  > Hello World↵ 
   
  
  # 문자열 입력받기
  data = sys.stdin.readline().rstrip()    # readline()은 엔터키를 줄바꿈 기호로 입력되는데, 이 공백문자를 rstrip()으로 제거
  print(data)    # Hello World
  
  ```
  
 
 - 출력을 할 때는 print() 함수를 이용하여 출력을 진행할 수 있다.
 - print()는 변수나 상수를 매개변수로 입력받아 이를 표준 출력으로 출력.
 - print()는 각 변수를 콤마(,)로 구분하여 매개변수로 넣을 수 있는데, 이 경우 각 변수가 띄어쓰기로 구분되어 출력된다.
 
     ```python
     # 출력할 변수들
     a = 1
     b = 2
     
     pirnt(a, b)     # 1 2
     ```
     
- 일부 문제의 경우 출력할 때 문자열과 수를 함께 출력해야 되는 경우가 있다. 이 경우 단순히 더하기 연산자(+)를 이용하여 문자열과 수를 더하면 오류가 발생

  ```python
  # 출력 시 오류가 발생하는 소스코드 예시
  # 출력할 변수들
  answer = 7
  
  print("정답은" + answer + "입니다.")
  ```

- 파이썬은 문자열과 수를 더할 때 자동으로 수 데이터가 문자열로 변환되지 않음

  ```python
  
  # 변수를 문자열로 바꾸어 출력하는 소스코드 예시
  # 출력할 변수들
  answer = 7
  
  print("정답은 " + str(answer) + "입니다")
  ```

- 각 변수를 콤마로 구분하여 출력하는 경우, 변수의 값 사이에 의도치 않은 공백이 삽입될 수 있다는 점을 신경 써주도록 하자.

  ```python
  # 출력할 변수들
  answer = 7
  
  print("정답은", str(answer), "입니다.")     # 정답은  7  입니다.
  


## 8. 주요라이브러리 문법과 유의점
- 파이썬의 일부 라이브러리는 잘못 사용하면 수행 시간이 비효율적으로 증가하므로 이 절에서 설명하는 내용을 잘 기억해두자.
- 표준 라이브러리란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미
- 코딩 테스트에서는 대부분 표준 라이브러리를 사용할 수 있도록 허용하므로 표준 라이브러리를 사용하면 소스코드 작성량에 대한 부담을 줄일 수 있다.


**코딩 테스트를 준비하며 반드시 알아야 하는 라이브러리는 6가지 정도이다.**

1. 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다. 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.

2. itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. **순열과 조합** 라이브러리를 제공한다.

3. heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용.

4. bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리

5. collections : 덱(deque), 카운터(counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

6. math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함.


## 내장 함수

- 별도의 import 명령어 없이 바로 사용할 수 있는 내장 함수가 존재.
- sum() : 리스트와 같은 iterable 객체가 주어졌을 때, 모든 원소의 합을 반환

- min() : 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환.
- max() : 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환.
- eval() : 수학 수식이  문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환

```python
  result = eval("(3+5) * 7")
  print(result)     # 56
```
- sorted() 함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환. key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정할 수 있다.

```python
    # 리스트 [9, 1, 8, 5, 4]를 오름차순으로 정렬하는 예시와 내림차순으로 정렬하는 예시는 다음과 같다
    
    result = sorted([9, 1, 8, 5, 4])    # 오름차순으로 정렬
    print(result)
    result = sorted([9, 1, 8, 5, 4], reverse = True)    # 내림차순으로 정렬
    print(result)
```


- 파이썬에서는 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다.
- 정렬 기준은 key 속성을 이용해 명시할 수 있다.
- 에를 들어 [('홍길동', 35), ('이순신', 75), ('아무개', 50)]이 있을 때, 원소를 튜플의 두 번째 원소를 기준으로 내림차순 정렬하고자 한다면 다음과 같이 사용할 수 있다.

```python
    result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x : x[1], reverse = True)
```    

- 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서 굳이 sorted() 함수를 사용하지 않고도 sort() 함수를 사용해서 정렬할 수 있다.
- 이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경된다.

```python
# 리스트 [9, 1, 8, 5, 4] 를 오름차순으로 정렬하는 예시는 다음과 같다.
data = [9, 1, 8, 5, 4]
data.sort()
print(data)    # [1, 4, 5, 8, 9]
```


## itertools
- 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
- permutations(순열) : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해 준다.
- permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
- 리스트 ['A', 'B', 'C'] 에서 3개 (r = 3)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

```python

  from itertools import permutations
  
  data = ['A', 'B', 'C']
  
  result = list(permutations(data, 3))  # 모든 순열 구하기    # 객체 초기화 후 리스트 자료형으로 변환해서 사용

  print(result)   #  ABC, ACB, BAC, BCA, CAB, CBA
```

- combinations(조합) : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)
- (순서를 고려하지 않는다 = 순서에 의미를 두지 않겠다 = 순서가 달라도 같은 걸로 간주하겠다. ex) ab = ba)
- combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
- 리스트 ['A', 'B', 'C'] 에서 2개 (r = 2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다. 

```python
    from itertools import combinations
    
    data = ['A', 'B', 'C']    # 데이터 준비
    result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합 구하기
    
    print(result)    # AB, AC, BC
```


- product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (순열) 을 계산한다.
- 다만 원소를 중복하여 뽑는다.
- product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
- product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
- product = 중복을 허용하여 repeat 개의 원소를 뽑기
- 리스트 ['A', 'B', 'C'] 에서 중복을 포함하여 2개 (r = 2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다. 


```python
    from itertools import product
    
    data = ['A', 'B', 'C']
    result = list(product(data, repeat = 2)  # 2 개를 뽑는 모든 순열 구하기 (중복 허용), 그냥 2개씩 뽑을 수 있는 모든 경우의 수
    
    print(result)    # AA, AB, AC, BA, BB, BC, CA, CB, CC
 ```
 
 
    
- combinations_with_replacement(조합) : combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)
- (순서를 고려하지 않는다 = 순서에 의미를 두지 않겠다 = 순서가 달라도 같은 걸로 간주하겠다. ex) ab = ba)
- combinations_with_replacement 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
- 리스트 ['A', 'B', 'C'] 에서 2개 (r = 2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다. 

```python
    from itertools import combinations_with_replacement
    
    data = ['A', 'B', 'C']    # 데이터 준비
    result = list(combinations_with_replacement(data, 2))    # 2개를 뽑는 모든 조합 구하기
    
    print(result)    # AA, AB, AC, BB, BC, CC
```
  


## heapq 
- 파이썬에서는 힙 기능을 위해 heapq 라이브러리를 제공한다. heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 **우선순위 큐** 기능을 구현하고자 할 때 사용된다.
- 파이썬의 힙은 최소 힙으로 구성되어 있으므로(최소 값을 가진 원소가 가장 위에 위치), 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
- 보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은 원소'이기 때문이다.
- **힙에 원소를 삽입할 때는 heapq.heappush(), 힙에서 원소를 꺼내고자 할 때는 heapq.heappop() 메서드를 이용한다.**
- 힙 정렬을 heapq로 구현하는 예제를 통해 heapq의 사용 방법을 알아보자.

```python
    import heapq
    
    def heapsort (iterable) :    # iterable 객체를 매개변수로 받음
        h = []    # 데이터를 넣을 배열
        result = []
        
        # 모든 원소를 차례대로 힙에 삽입
        
        for value in iterable :
            heapq.heappush(h, value) = h를 힙으로 사용하여 원소를 삽입
            
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        for i in range(len(h)) :    # 힙의 원소의 개수 만큼 반복
            result.append(heapq.heappop(h))    
        return result
        
    
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
```


- 또한 파이썬에서는 최대 힙을 제공하지 않는다.
- 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.
- 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.
- 이러한 방식으로 최대 힙을 구현하여 내림차순 힙 정렬을 구현하는 예시는 다음과 같다.
    
    
    
```python
    import heapq
    
    def heapsort (iterable) :    # iterable 객체를 매개변수로 받음
        h = []    # 데이터를 넣을 배열
        result = []
        
        # 모든 원소를 차례대로 힙에 삽입
        
        for value in iterable :
            heapq.heappush(h, -value) = h를 힙으로 사용하여 원소를 삽입
            
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        for i in range(len(h)) :    # 힙의 원소의 개수 만큼 반복
            result.append(-heapq.heappop(h))    
        return result
        
    
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)    # 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    
```


## bisect
- 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. bisect 라이브러리는 **"정렬된 배열"** 에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
- bisect 라이브러리에서는 **bisect_left() 함수와 bisect_right() 함수**가 가장 중요하게 사용되며, 이 두 함수는 시간 복잡도 O(logN)에 동작한다.

- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a 에 데이터 x 를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a 에 데이터 x 를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

- 예를 들어 정렬된 리스트 a = [1, 2, 4, 4, 8] 이 있을 때, 새롭게 데이터 4를 삽입하려 한다고 가정하자.
- 이때 bisect_left(a, 4)와 bisect_right(a, 4)는 각각 인덱스 값으로 2와 4를 반환한다.

```python
  from bisect import bisect_left, bisect_right
  
  a = [1, 2, 4, 4, 8]
  x = 4
  
  print(bisect_left(a, x))    # 2
  print(bisect_right(a, x))    # 4
```

- 또한 bisect_left() 함수와 bisect_right() 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용될 수 있다.
- 아래의 count_by_range(a, left_value, right_value) 함수를 확인해보자
- 이는 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환한다.
- 다시 말해 원소의 값을 x 라고 할 때, left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산할 수 있다.

```python
    from bisect import bisect_left, bisect_right
    
    # 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
    def count_by_range(a, left_value, right_value) :
       right_index = bisect_right(a, right_value)   # right_value 값의 오른쪽 인덱스를 반환
       left_index = bisect_left(a, left_value)    # left_value 값의 왼쪽 인덱스를 반환
       
       return right_index - left_index
       
   # 리스트 선언
   a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
   
   # 값이 4인 데이터 개수 출력
   print(count_by_range(a, 4, 4))    # 8 - 6 = 2
   
   # 값이 [-1, 3] 범위에 있는 데이터의 개수 출력
   print(count_by_range(a, -1, 3))    # 6 - 0 = 6
   
```



## collections 

- 파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다.
- collections 라이브러리의 기능 중에서 코딩 테스트에서 유용하게 사용되는 클래스는 deque와 Counter 이다.


## deque - 양 끝에 삽입, 삭제를 할 수 있는 Queue

- 보통 파이썬에서는 deque를 사용해 큐를 구현한다.
- 별도로 제공되는 Queue 라이브러리가 있는데 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다.
- 따라서 deque를 이용해 큐를 구현해야 한다는 점을 기억하자.

- 기본 리스트 자료형은 데이터의 삽입, 삭제 등의 다양한 기능을 제공한다.
- 리스트가 있을 때 중간에 특정한 원소를 삽입한느 것도 가능하다.
- 하지만 리스트 자료형은 append() 메서드로 데이터를 추가하거나, pop() 메서드로 데이터를 삭제할 때 '가장 뒤쪽 원소'를 기준으로 수행된다.
- 따라서 앞쪽에 있는 원소를 처리할 때에는 리스트에 포함된 데이터의 개수에 따라서 많은 시간이 소요될 수 있다.
- 리스트에서 앞쪽에 있는 원소를 삭제하거나 앞쪽에 새 원소를 삽입할 때의 시간 복잡도는 O(N)이다.

- deque는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다.
- 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다.
- 따라서 deque를 큐 자료구조로 이용할 때, 원소를 삽입할 때에는 append()를 사용하고 원소를 삭제할 때에는 popleft()를 사용하면 된다.
- 그러면 먼저 들어온 원소가 항상 먼저 나가게 된다.
- 리스트 [2, 3, 4]의 가장 앞쪽과 뒤쪽에 원소를 삽입하는 예시는 다음과 같다.

```python
    from collections import deque
    
    data = deque([2, 3, 4])
    data.appendleft(1)    # 첫번째 인덱스에 원소 삽입
    data.append(5)    # 마지막 인덱스에 원소 삽입
    
    print(data)    # deque([1, 2, 3, 4, 5])
    print(list(data))    # 리스트 자료형으로 변환 [1, 2, 3, 4, 5]
```


## Counter

- 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다. 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
- 따라서 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 이를 구현할 수 있다.


```python
    from collections import Counter
    
    counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])    # 리스트를 매개변수로 전달
    
    print(counter['blue'])    # blue가 등장한 횟수 출력 - 3
    print(counter['green'])    # green이 등장한 횟수 출력 - 1
    print(dict(counter))    # 사전 자료형으로 변환 (키-등장 횟수) - {'red' : 2, 'blue}
```



## math
- math 라이브러리는 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
- 팩토리얼, 제곱근, 최대공약수(GCD) 등을 계산해주는 기능을 포함, 수학 계산을 요구하는 문제를 만났을 때 효과적으로 사용될 수 있다.

```python
   import math
   
   print(math.factorial(5))    # 5 팩토리얼을 출력 - 120

```

- sqrt(x) 함수는 x의 제곱근을 반환
```python
   import math
   
   print(math.sqrt(7))    # 7의 제곱근을 출력 - 2.6457513....
   

```

- 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd(a, b) 함수를 이용
- 이 함수는 a와 b의 최대 공약수를 반환한다.

```python
   import math
   
   
   print(math.gcd(21, 14))    # 21과 14의 최대 공약수 - 7
```

- 수학 공식에서 자주 등장하는 상수가 필요할 때에도 math 라이브러리를 사용할 수 있다.
- math 라이브러리는 파이(pi)나 자연상수 e를 제공

```python
   import math
   
   
   print(math.pi)    # 파이 출력
   print(math.e)    # 자연상수 e 출력
```


## 당장 좋은 것만 선택하는 그리디
- 그리디 알고리즘은 단순하지만 강력한 문제 해결 방법
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미
- 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.
- **사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형**
- 특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는지를 파악할 수 있어야 한다.
- 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.
- 대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다.



  ### 거스름돈
  당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
  
### 문제해설
> '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것.

```python
n = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types :
  count += n // coin    # n을 거스름돈으로 나눈 몫
  n %= coin

print(count)

```

- 코드를 보면 화폐의 종류만큼 반복을 수행
- 화폐의 종류가 K개라고 할 때 위 소스코드의 시간 복잡도는 O(K)
- 시간 복잡도에서 거슬러 주어야 할 돈 N은 찾아볼 수 없다.
- 즉, 이 알고리즘의 시간 복잡도는 동전의 총 종류에만 영향을 받고, 거슬러 줘야하는 금액의 크기와는 관

### 그리디 알고리즘의 정당성
- 대부분의 문제는 그리디 알고리즘을 이용했을 때 "최적의 해"를 찾을 수 없을 가능성이 다분하다.
- 하지만 거스름돈 문제에서 "가장 큰 화폐 단위부터" 돈을 거슬러 주는 것과 같이, 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 때는 매우 효과적
- 그리디 알고리즘으로 문제의 해법을 찾았을 때는 그 해법이 정당한지 검토해야 한다,
- 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로, 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
- 어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 **그리디 알고리즘을 의심**하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해보자.
- 오랜 시간을 고민해도 그리드 알고리즘으로 해결 방법을 찾을 수 없다면, 다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지를 재차 고민해보는 것도 한 방법
- 처음에 문제를 만났을 때는 이것저것 다양한 아이디어를 고려해야 한다.


### 큰 수의 법칙
 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다. 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서 세 번 까지 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4 + 4 + 4 + 4 + 4 + 4 + 4 인 28이 도출된다.

> 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.


> 입력 조건 : 첫 째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), k(1<= k <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
             둘째 줄에 N 개의 자연수가 주어진다. 각 자연수는 공백으로 구분하낟. 단 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
             입력으로 주어지는 k는 항상 M보다 작거나 같다.
             
> 입력 예시
> 5 8 3

```python
# N개의 수를 공백으로 구분하여 입력 받기
n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)

first = data[0]
second = data[1]

result = 0
count = 0

for _ in range(m) :
 
  if count == k :
    result += second
    count = 0
  else :
    result += first
    count += 1
  
  
print(result)
```

- 이 문제는 M이 10,000 이하이므로 이 방식으로도 문제를 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
- 간단한 수학적 아이디어를 이용해 더 효율적으로 문제를 해결해보자. 

- 예를 들어 N이 5이고 입력 값이 2, 4, 5, 4, 6 이 주어졌다고 가정하자.

- 이 때 가장 큰 수와 두 번째로 큰 수를 선택하면 다음과 같다.
  - 가장 큰 수 : 6
  - 두 번째로 큰 수 : 5

- 이 때 M이 8이고, K가 3이라면 다음과 같이 더했을 때 합을 최대로 할 수 있다. 다시 말해 (6+6+6+5) + (6+6+6+5)로 정답은 46이 된다.
- 이 문제를 풀려면 가장 먼저 반복되는 수열에 대해서 파악해야 한다.
- 가장 큰 수와 두 번재로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
- 따라서 M을 (k + 1)로 나눈 몫이 수열이 반복되는 횟수가 된다.
- 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.

이 문제를 풀려면 가장 먼저 반복되는 수열에 대해서 파악해야 한다.
가장 큰 수와 두 번쨰로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
위의 예시에서는 수열 [6, 6, 6, 5]가 반복된다.
그렇다면 반복되는 수열의 길이는 어떻게 될까? 바로 (K + 1)로 위의 예시에서는 4가 된다.

따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 된다.
다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다. # 수열 하나에 가장 큰 수가 K 번 등장하므로, 위의 예시에서는 2 X 3 = 6번
이때 M이 (K + 1)로 나누어떨어지지 않는 경우도 고려해야 한다. 그럴 때는 M을 (K+1)로 나눈 나머지 만큼 가장 큰 수가 추가로 더해지므로 이를 고려해 주어야 한다.

즉, 가장 큰 수가 더해지는 횟수는 다음과 같다

    int( (M / (K+1)) * K + M % (K+1)

결과적으로 위의 식을 이용하여 가장 큰 수가 더해지는 횟수를 구한 다음, 이를 이용해 두 번째로 큰 수가 더해지는 횟수까지 구할 수 있는 것.

```python
 # N개의 수를 공백으로 구분하여 입력 받기
n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()    # 입력받은 수 정렬
 
fisrt = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k 
count += m % (k + 1)

result = 0
result += fisrt * count # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
```


### 구현 
- 코딩 테스트에서 구현이란 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다.
- 어떤 문제를 풀든 간에 소스코드를 작성하는 과정은 필수이므로 구현 문제 유형은 모든 범위의 코딩 테스트 문제 유형을 포함하는 개념이다.
- 흔히 구현 유형의 문제는 '풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제'를 의미한다.
- 사소한 조건 설정이 많은 문제일수록 코드로 구현하기가 까다롭다.
- 완전 탐색, 시뮬레이션 유형을 모두 '구현' 유형으로 묶어서 다루고 있다.
- **완전 탐색**은 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
- **시뮬레이션**은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형
- 보통 구현 유형의 문제는 사소한 입력 조건 등을 문제에서 명시해주며 문제의 길이가 꽤 긴 편이다.
- 문제의 길이를 보고 지레 겁먹는데, 고차원적인 사고력을 요구하는 문제는 나오지 않는 편이라 문법에 익숙하다면 오히려 쉽게 풀 수 있다.


- **ord(문자) : 문자에 맞는 아스키 코드 값 반환**
- **char(아스키코드) : 아스키 코드에 맞는 문자 반환**



### DFS/BFS
- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미한다.
- 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다.
- 대표적인 탐색 알고리즘으로는 **DFS와 BFS**를 꼽을 수 있는데 이 두 알고리즘의 원리를 제대로 이해해야 코딩 테스트의 탐색 문제 유형을 풀 수 있다.
- 그런데 DFS와 BFS를 제대로 이해하려면 기본 자료구조인 스택과 큐에 대한 이해가 전제되어야 하므로 사전 학습으로 스택과 큐 , 재귀 함수를 간단히 정리하고자 한다.

- 자료구조(Data Structure)란 데이터를 표현하고 관리하고 처리하기 위한 구조
- 스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심적인 함수로 구성된다
  - 삽입(Push) : 데이터를 삽입한다.
  - 삭제(Pop) : 데이터를 삭제한다.

- 물론 실제로 스택과 큐를 사용할 때는 삽입과 삭제 외에도 오버플로와 언더플로를 고민해야 한다.
- **오버플로**는 자료구조가 가득 찬 상태에서 삽입 연산을 수행할 때 발생.
- 즉, 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생한다.
- **언더플로** 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 발생.

- 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다.
- 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.

- 큐는 대기 줄에 비유할 수 있다.
- 선입선출 구조이다

```python

# 큐 예제
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 - 3, 7, 1, 4
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 - 4, 1, 7, 3

- 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자.
- deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.


### 재귀 함수
- DFS와 BFS를 구현하려면 재귀 함수도 이해하고 있어야 한다
- 재귀 함수란 자기 자신을 다시 호출하는 함수를 의미한다.

```python
# 재귀함수 예제
def recursive_func() :
  print("재귀 함수를 호출합니다")
  recursive_func()
  
recursive_func()  
```

### 재귀 함수의 종료 조건
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, **종료 조건을 꼭 명시해야 한다.**
- 다음은 재귀 함수를 100번 호출하도록 작성한 코드이다. 재귀 함수 초반에 등장하는 if 문이 종료 조건 역할을 수행한다.

```python
def recursive_function(i) :
  # 100번째 출력했을 때 종료되도록 종료 조건 명시
  if i == 100 : 
    return
  
  print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
  recursive_function(i+1)
  print(i, "번째 재귀 함수를 종료합니다.")
```

- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.
- 재귀 함수를 이용하는 대표적 예제로는 팩토리얼 문제가 있다.

```python

# 2가지 방식으로 구현한 팩토리얼 예제

# 반복문으로 구현한 n!

def factorial_iterative(n) :
  result = 1
  
  # 1 부터 n 까지의 수를 차례대로 곱하기
  for i in range(1, n + 1) :
     result *= i

# 재귀적으로 구현한 n!
def factorial_recursive(n) :
  if n <= 1 :
    return 1
  # n! = n * (n-1)!
  return n * factorial_recursive(n-1)
```

- 재귀 함수의 코드가 더 간결한 것을 알 수 있다.
- 이렇게 간결해진 이유는 재귀 함수가 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문이다. 
- 수학에서 점화식은 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미한다.

- 일반적으로 우리는 점화식에서 종료 조건을 찾을 수 있는데, 앞 예시에서 종료 조건은 n이 0 혹은 1일 때 이다.


### DFS (Depth First Search, 깊이 우선 탐색)
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

- 그래프는 노드(Node)와 엣지(Edge)로 표현되며 이때 노드를 정점(Vertex)이라고도 말한다.
- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.
- 또한 두 노드가 간선으로 연결되어 있다면 두 노드는 인접하다(Adjacent)라고 표현한다.

- 프로그래밍에서 그래프는 크게 2가지 방식으로 표현할 수 있는데, 코딩 테스트에서는 이 두 방식 모드 필요하니 두 개념에 대해 바르게 알고 있도록 하자.
- **인접 행렬(Adjacency Matrix)** : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- **인접 리스트(Adjacency List)** : 리스트로 그래프의 연결 관계를 표현하는 방식

- 먼저 인접 행렬(Adjacency Matrix) 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.
- 연결이 되어 있지 않은 노드끼리는 무한의 비용이라고 작성하낟.
- 실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 987654321 등의 값으로 초기화 하는 경우가 많다.


```python
INF = 9999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
  [0, 7, 5],   # 0번 노드에 대한 연결 정보
  [7, 0, INF], # 1번 노드에 대한 연결 정보
  [5, INF, 0 ] # 2번 노드에 대한 연결 정보
 ]

```


- 그렇다면 인접 리스트(Adjacency List) 방식에서는 데이터를 어떤 방식으로 저장할까 ?
- 인접 리스트 방식에서는 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.
- 인접 리스트는 '연결 리스트'라는 자료구조를 이용해 구현하는데, 파이썬은 기본 자료형이 append()와 메소드를 제공하므로, 배열과 연결 리스트의 기능을 모두 기본으로 제공한다.
- 파이썬으로 **인접 리스트를 이용해 그래프를 표현하고자 할 때에도** 단순히 **2차원 리스트를 이용하면 된다는 점**만 기억하자.


```python

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]   # 노드가 총 3개 이므로 모든 노드에 대해 연결 정보를 입력하려면 3행을 가진 리스트로 초기화 해야함

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7)) - (노드, 거리) 값이 담긴 리스트를 노드 0의 정보에 추가
graph[0].append((2, 5)) 

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7)) - (노드, 거리) 값이 담긴 리스트를 노드 1의 정보에 추가


# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5)) - (노드, 거리) 값이 담긴 리스트를 노드 2의 정보에 추가
```

- 두 방식은 어떤 차이가 있을까?
- 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 때 불필요하게 메모리를 낭비.
- 반면에 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용
- 하지만, 이와 같은 속성 때문에 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 잇는지에 대한 정보를 얻는 속도가 느림.
- 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문
- 그러므로 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.

- DFS는 깊이 우선 탐색 알고리즘이라고 했다.
- 이 알고리즘은 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.
- DFS는 스택 자료구조를 이용하며 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.

- DFS를 이용하여 탐색하면, 일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다.

```Python
 # DFS 메서드 정의 ( 스택으로 구현 )
 def dfs(graph, v, visited) :   # graph = 그래프 정보, v = 현재 노드, visited = 방문 정보 
     # 현재 노드를 방문 처리
     visited[v] = True
     print(v, end=' ')    # 방문한 노드 출력
     
     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
     for i in graph[v] :
         if not visited[i] :  # 방문한 적이 없을 때만 방문
             dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트 = 인접 리스트 방식)
graph = [
[], # 0 번 노드는 비어있음, 1번 노드부터 사용할 것이기 때문에
[2, 3, 8],
[1, 7],
[1, 4, 5],
[3, 5],
[3, 4],
[7],
[2, 6, 8],
[1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9   # False로 노드 개수만큼 크기를 가진 배열로 초기화

# dfs 함수 호출
dfs(graph, 1, visited) # 1번 노드를 시작 노드로 지정   # 1 2 7 6 8 3 4 5
```

## BFS (Breadth First Search)

BFS(Breadth First Search) 알고리즘은 '너비 우선 탐색' 이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데, BFS는 그 반대다. 
BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다. 
알고리즘의 정확한 동작 방식은 다음과 같다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 위의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.

```Python
from collections import deque # 파이썬에서 큐는 collections의 deque를 이용해서 구현

# BFS 메서드 정의
def bfs(graph, start, visited) : # graph = 그래프 정보, start = 시작 노드, visited = 방문 정보
    # deque 라이브러리를 이용해 큐를 구현
    queue = deque([start])    # 최초 시작 노드를 큐에 삽입
   
   # 현재 노드를 방문 처리
    visited[start] = True
   
   # 큐가 빌 때 까지 반복 
   while queue :   # iterable 객체를 조건문에 사용하면 원소가 있으면 반복
       # 큐에서 원소를 하나 뽑아 출력
       v = queue.popleft() # popleft로 제일 먼저 들어온 원소를 선택
       print(v, end=' ')
       
       # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
       for i in graph[v] :
           if not visited[i] :
                queue.append(i) 
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트 = 인접 리스트 방식)
graph = [
[], # 0 번 노드는 비어있음, 1번 노드부터 사용할 것이기 때문에
[2, 3, 8],
[1, 7],
[1, 4, 5],
[3, 5],
[3, 4],
[7],
[2, 6, 8],
[1, 7]
] 

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9   # False로 노드 개수만큼 크기를 가진 배열로 초기화

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)


```


### DFS vs BFS

||DFS|BFS|
|:---:|:---:|:---:|
|동작 원리|스택|큐|
|구현 방법|재귀 함수 이용|큐 자료구조 이용|

1차원 배열이나 2차원 배열을 그래프 형태로 생각하면 수월하게 문제를 풀 수 있다. 특히나 DFS와 BFS 문제 유형이 그러하다.
예를 들어 게임 맵이 3 X 3 형태의 2차원 배열이고 각 데이터를 좌표라고 생각해보자. 게임 캐릭터가 (1,1) 좌표에 있다고 표현할 떄 처럼 말이다.
코딩 테스트 중 2차원 배열에서의 탐색 문제를 만나면 이렇게 그래프 형태로 바꿔서 생각하면 풀이 방법을 조금 더 쉽게 떠올릴 수 있다. 그러므로 코딩 테스트에서 탐색 문제를 보면 그래프 형태로 표현한 다음 풀이법을 고민하도록 하자.
=> 배열에서의 탐색 문제는 배열을 그래프로 표현하면 쉽게 풀이 가능


### 음료수 얼려 먹기

N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

> 입력
> 00110
> 00011
> 11111
> 00000

0으로 연결된 공간의 개수를 구하면 됌, 배열에서의 탐색 문제 > 배열을 그래프로 표현하여 해결
> 입력 N, M 은 1 ~ 1,000 의 값
> 최대 1,000 X 1,000 = 1,000,000 원소 = 완전 탐색이 가능한 수준
> 시작 원소를 기준으로 DFS 탐색을 수행하며 0인 원소를 1로 변환
> 다음 원소로 이동해서 반복, 이 때 해당 원소가 0이면 0으로 연결된 공간이므로 count + 1
> (BFS로 구현하려면 원소간 연결 정보가 필요한데, 배열의 모든 원소에 대한 연결 정보를 변환하는 작업 없이 DFS로 구현하는게 더 간단)
> (DFS로 구현시, 연결 정보 없이 상, 하, 좌, 우에 대해서 반복적으로 확인해보면 됌)
> 
```python

n, m = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append( list(map(int, input())))  


def dfs (x, y) :
    # 갈 수 없는 위치이면 False

    if x < 0 or x >= n or y < 0 or y >= m :
   
        return False
      
    # 모든 탐색을 마치면 True
    if graph[x][y] == 0 : 
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    # 이미 방문했던 위치라면 False  
    return False


result = 0
for x in range(n) : 
    for y in range(m) :
        if dfs(x, y) == True :
            result += 1

print(result)
    
  
```    


### 미로 탈출
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1,1) 이고 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다. 이 때 괴물이 있는 부분은 0 으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이 때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

### 문제 해설
이 문제는 BFS를 이용했을 때 매우 효과적으로 해결할 수 있다. BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다. 그러므로 (1,1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다. 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.
즉, BFS를 이용하여 시작 노드부터 모든 인접 노드들을 탐색하며 거리 정보를 노드에 업데이트 하고, 최종적으로 출구 까지의 거리 정보를 반환






  

