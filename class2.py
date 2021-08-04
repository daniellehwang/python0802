# class2.py
#클래스를 정의
class Person:
    #공유 데이터로 사용(C#의 static멤버변수)
    num_person = 0
    def __init__(self):
        self.name ="default name"
        #카운트를 하는 코드
        Person.num_person += 1
    def print(self):
        print("My name is {0}". formate(self.name))

#인스턴스 생성
p1 = Person()   # 쿠키 찍어냄
p2 = Person()
p3 = Person()

print("인스턴스 갯수:{0}".format(Person.num_person))