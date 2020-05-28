# #1 이름 5가지 목록 리스트에 넣고, 반복문 2가지로 프린트
#
# name = ['조지헌', '김지헌', '송지헌', '유지헌', '마지헌']
# for x in name:
#     print(x)
#
# #2 1부터 10까지를 더하세요.
#
# sum = 0
# for x in range(0, 10):
#     sum = x + sum
# print(sum)
#
# #3 5개의 정수를 입력받아 더해서 프린트
#
# data = []
# for i in range(0,5):
#     data.append(int(input("숫자 입력해주세용 : ")))
# print(data)
#
# #4 숫자를 10개 입력받아 그 중 5 이상인 갯수를 프린트
#
# data = []
# for y in range(0,10):
#     data.append(int(input("숫자 입력해주세용 : ")))
#
# for h in data:
#     if h >= 5:
#         print(h)
#
# #5 처음시작 숫자와 마지막 숫자만큼 별 찍기
# s_num = int(input("처음 시작 숫자"))
# l_num = int(input("마지막 숫자"))
#
# for p in range(s_num, l_num):
#     print("★")
#
#

#1. 13이 홀수인지 짝수인지 판별법

if 13 % 2 == 1 :
    print("홀수입니다.")
else:
    print("짝수입니다.")

#2. 주민번호 8811220-1068234임. 남성/여성 판별

ssn = "881220-1068234"
if ssn[7] == "1":
    print("남자입니다.")
else:
    print("여자입니다.")

#3 22,44,66,11,99 중 최대값을 함수를 써서 찾으세요.
nums = [22,44,66,11,99]
print(max(nums))

#4. 시험공고 기간 중 시험성적 공고는 변경불가능한 타입으로 다음을 저장하시오.

date = (99,11,55,22,88)
print(type(date))
print(date)

#타입변경

date_list = list(date)
date_list[0] = 100
print(date_list[0])
print(type(date_list))

#5. id는 root, pw는 1234, name은 홍길동, tel은 888-1234 위의 데이터를 저장하기 위한 적절한 타입을 선택 후 저장
# name에 해당하는 값 출력, 위 사람에 대한 값만 모두 출력

me = dict() #딕셔너리 선언
me['id'] = 'root'
me['pw'] = 1234
me['name'] = '홍길동'
me['tel'] = '888-1234'
print(me['name'])
print(me)

#6. 각 반의 수학 시험 결과입니다. c1 => 22,99,11,23 // c2 => 44, 99, 24, 55

c1 = [22,99,11,23]
c2 = [44,99,24,55]
print(c1+c2)

c1_set = set(c1)
c2_set = set(c2)
print(c1_set.intersection(c2))

#7 def
