class Dog:
    name = '코코'
    age = 2
    def bark(self):
        print('멍멍')
    def move(self):
        print('움직인다')
    def eat(self):
        print('먹는다')
dog1 = Dog()
dog1.bark()
dog1.bark()
dog1.move()
dog1.eat()
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name, self.age)
        print('멍멍')
    def move(self):
        print('움직인다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence
dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
dog1.bark()
dog2.bark()
print(dog1)
print(dog2)
result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def divi(self, num):
        self.result /= num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal2.add(3))
print(cal1.add(4))
print(cal2.add(4))
print(cal1.sub(1))
print(cal2.sub(1))
print(cal1.mul(3))
print(cal1.mul(10))
print(cal1.divi(2))
print(cal1.divi(9))
print(cal2.mul(3))
print(cal2.mul(10))
print(cal2.divi(2))
print(cal2.divi(9))
class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self):
        print('랄랄라')
    def eat(self):
        print('먹는다')
bird1 = Bird('코코', 2)
bird2 = Bird('두리', 4)
print(bird1.name, bird1.age)
print(bird2.name, bird2.age)
bird1.sing()
bird2.eat()
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age, self.owner)
        return sentence
dog = Dog('코코', 2, '홍길동')
dog.eat()
dog.move()
dog.bark()
dog.shake()
print(dog)
