'''

문제 설명
우리말을 쓰는 평범한 사람이라면 1억원, 1조원을 일억 원, 일조 원이라고 읽지 억원, 조원이라 읽지 않습니다. 반면에 1만원, 1천원, 1백원의 경우는 일만 원, 일천 원, 일백 원이라 읽지 않고 만원, 천원, 백원, 십원이라 읽습니다.

또한 ‘80,270원’처럼 금액의 표기는 천 단위로 콤마를 찍지만 실제로 읽을 때는 ‘팔만 이백칠십원’처럼 만 단위로 분리하여 읽습니다.

“배조스님의 계좌에서 사이냅소프트님의 계좌로 일조 사천 일백 팔십 오억 원을 이체합니다. 동의하시면 1번을…”

계좌이체 음성안내의 부자연스러운 금액 표현과 띄어 읽기가 거슬렸던 암아존 배조스씨를 위해 이체금액을 한글로 자연스럽게 읽을 수 있는 프로그램을 작성해서 보내주세요. 프로그래밍 언어는 가장 자신 있는 것을 사용하세요.

 

– 입력
암아존 배조스님의 은행 이체한도는 100조원으로 설정돼 있으므로 입력 금액의 범위는 1원에서 100조원까지입니다. 모든 금액은 천 단위 구분자인 콤마가 표시돼있고 금액단위인 원으로 끝납니다.

예로 아래와 같은 입력이 가능합니다. 입력은 별도 파일에서 읽어와도 되고, 소스코드 안에 포함시켜도 됩니다. 물론 UI를 만들어 사용자로부터 직접 입력을 받아도 좋습니다.

1원
80,270원
111,111원
1,234,567,890원
100,000,000,000,000원
– 출력
입력에 대하여 만 단위 띄어쓰기로 구분된 자연스러운 한글읽기를 출력합니다.

위 예의 출력은 다음과 같습니다.

일원
팔만 이백칠십원
십일만 천백십일원
십이억 삼천사백오십육만 칠천팔백구십원
백조원



'''



input = "1,234,567원"

input = input[0:-1].replace(",", "")
input = input.rjust(16,"0")
input = list(input)

# 0~3 4~7 8~ 11 12~15

num_to_read = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
unit_1 = ["조_", "억_", "만_", "원_"]
unit_2 = ["천", "백", "십", ""]

result = []

chunk_size = 4
input = [ input[i : i + chunk_size] for i in range(0, len(input), chunk_size)]

print(input)

for idx, nums in enumerate(input) :
    nums_str = "".join(nums)
    nums_int = int(nums_str)

    if nums_int > 0 :
      
        for idx_num, num in enumerate(nums) :
            num_int = int(num)

            if num_int > 0 :
                result.append(num_to_read[num_int] + unit_2[idx_num])
                
              
        result.append(unit_1[idx])


#result = "".join(result)

for idx, text in enumerate(result) :
    if text == "일십" :
        result[idx] = "십"
    elif text == "일백" :
        result[idx] = "백"  
    elif text == "일천" :
        result[idx] = "천"  
    elif text == "일만" :
        result[idx] = "만"  



print("".join(result).replace("_"," "))


