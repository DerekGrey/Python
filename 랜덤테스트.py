import random

#print(random.randint(0,10)) #randint만 0~10까지
#print(random.randrange(0,10)) #0~9까지
#print(random.choice(['가위','바위','보'])) #1,2,3 중 랜덤으로 뽑아주렴

person1 = list()
for x in range(0,5):
    person1.append(random.randint(50, 100))
print(person1)

#10명을 리스트에 묶으세요?

#list() = [] 똑같음
personList = list() #전체 함수의 점수 목록
random.seed(100)
for y in range(0,1000) : #포문 0부터 1000까지돌림.
    person2 = list() #person2 에 변수 초기화
    for x in range(0,5): #
        person2.append(random.randint(50, 100))
    personList.append(person2)

print(len(personList), '명')
print('----------------')

sum = 0
for person in personList :
    print(person[0])
    sum = sum + person[0]

print(sum/len(personList))

###########################

print('--------------------')
file = open('total.txt', 'w') #write 쓰기모드
for person in personList:
    file.write(str(person)) #리스트를 스트링으로 캐스팅
    file.write('\n')

file2 = open('total.txt', 'r') #읽기모드
#print(file2.readline())

row1 = file2.readline()
print(row1)
print('--------------------')
str1 = row1.split(", '\n']")
print(type(str1))
print(str1[0])
person2 = list(str1)
print(person2)
print(type(person2))
print(person2[0])


# total = 0
# for person in personList:
#     row = file2.readlines()
#     listRow = list(row)
#     print(listRow)
#     test = listRow.split(",")
#     print(test)
#    # total = lastNum + total
# print(total)