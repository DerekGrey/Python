class Mom:
    doing = ''
    like = ''

    def tour(self):
        print("여행을 간다.")

    def free(self):
        print("자유시간을 즐긴다.")

    def __str__(self):
        return self.doing + ',' + self.like

class Girl: #클래스 선언
    name = '' #파이썬의 변수 초기값은 사용될때 만들어짐.
    age = 0
    
    def seat(self): #클래스에 있는 멤버함수라는 뜻, 멤버함수라 셀프라는 변수가생김.
        print("소녀가 앉아있다.")
    def tv(self):
        print("TV를 보고있다.")

    def __str__(self): #오버라이딩은 웬만하면 맨 아래
        return(self.name + ',' +  str(self.age)) #age 타입이 int였기 때문에

girl2 = Girl()
girl2.age = 30
girl2.name = '조조'
girl2.seat()
girl2.tv()

if __name__ == '__main__':
    girl1 = Girl()
    girl1.age = 10 
    girl1.name = '홍길순'
    print(girl1)

    girl1.seat()
    girl1.tv()

    mom = Mom()
    mom.doing = '운동'
    mom.like = '음식'
    print(mom)
    mom.free()
    mom.tour()