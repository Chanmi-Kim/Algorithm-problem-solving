'''
비타알고] 03월 1주차: 인싸가 되고 싶은 민수 ★2

어느 한 연구결과에 의하면 어느 대회에서 1등을 한 사람은 그 다음 대회에선 2등을 할 확률이 높고, 2등을 한 사람은 그 다음 대회에 1등을 할 확률이 높다고 합니다.

당신은 이 연구결과가 진실인지 확인하기 위해 임의의 대회에 출전한 한 사람의 등수 내역을 순서대로 나열해보았습니다. 이 대회는 9명 이하의 선수가 참가하기 때문에 등수는 1 이상 9 이하입니다. 등수를 나열한 이 문자열에서 "12"와 "21"의 부분 문자열이 각각 1번 이상 존재하면 이 연구결과는 맞다고 판단하고, 그렇지 않다면 틀리다고 판단합니다. 또한, 이 문자열이 서로 겹쳐서는 안 됩니다. 예를 들어, "2112"의 경우 21과 12를 각각 찾을 수 있지만, "212"의 경우 21을 찾으면 12를 못 찾고, 12를 찾으면 21을 찾지 못합니다.

이 연구결과의 진실 여부를 낱낱이 파헤쳐봅시다.

입력]

첫째 줄에 1 이상 9 이하의 숫자로 이루어진 문자열이 주어지며, 이 문자열의 길이는 1 이상 10^9 이하입니다.

출력]

연구결과가 참이면 Yes, 거짓이면 No를 출력합니다.
'''
'''
- 파일명 : Groom_the first and second_2nd-week-of-March.py
- 작성자 : KCM
- 작성일자 : 2019.08.28.
- 문제 : 구름EDU 19년 03월 위클리 비타알고
        03월 2주차: 1등과 2등 ★2 (https://bit.ly/2MKHDji)
- 난이도 : ★★☆☆☆
- 후기 : 정규표현식 사용법만 안다면 쉽게 풀 수 있는 문제였다.
        중간에 아무 문자열이 와도 된다는 .*를 몰랐다면 못 풀었을 것 같다.
'''

import re

numbers = input()
p = re.compile('.*21.*12.*|.*12.*21.*')
m = p.match(numbers)

if m is None:
	print("No")
else:
	print("Yes")
