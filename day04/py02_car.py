# py02_car.py

# 객체지향

class Car:
    # 속성값 모를 때는 None
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company  # 멤버변수 이름 앞에 __ 쓰면 외부 접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성')
    
    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제 차는 {self.__name}이고, 차번호는 {self.__plateNumber} 입니다.'
    
    def setPlateNumber(self, newPlateNumber='몰라용'): # 맞는 데이터가 들어오나 파악
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber
    
    def setName(self, newName='글쎄요'): # 모르면 글쎄요
        if type(newName) is str:
            self.__name = newName
    
    def getName(self):
        return self.__name


##모듈화를 위한 예제 소스 주석처리
# # myCar = Car('현대차', '아이오닉', '54라9537')
# myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대차')

# print(myCar) # 차의 번호를 출력하고 싶어

# myCar.__plateNumber = 2018 # 클래스 외부에서 잘못된 데이터를 넣어도 문제 발생 x
# print(myCar) # 그래서 안 된다.

# myCar.setPlateNumber('54라9999')
# print(myCar) # 된다.


# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumber('285구8899')
# print(yourCar)
# yourCar.setName('소나타')
# print(yourCar)