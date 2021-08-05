# class2.py
#클래스를 정의
from abc import abstractproperty


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

#동적으로 확장이 된다.
Person.title = " new title"
print(p1.title)
print(p2.title)
print(Person.title)
#인스턴스에 추가
p1.age = 30
print(p1.age)
#print(p2.age)

# *컴파일러: C, C++, C#, VB.NET
# 소스코드 ------------------> *exe,*.dll,*.app
#           (빌드, 만들기, 컴파일)
# 책을 번역하는 느낌(정적인 형식의 언어)

# *인터프리터(스크립트): python, R, JavaScript
# 소스를 직접 라인단위로 해석해서 실행
# 통역을 하는 느낌(동적으로 형식이 확장된다).