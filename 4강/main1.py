hello = "안녕하세요! 오늘은 기분이 좋습니다."
print(hello[5])
a = 472
b = 385
c = b%10*a
d = (b%100-b%10)//10*a
e = (b-b%100)//100*a
f = a*b
print(c, d, e, f)
letters = 'python'
print(letters[0], letters[2])
license_plate = "24가 1234"
print(license_plate[4:])
L = 'Life is too short, You need Python'
print(L[0], L[8], L[2], L[9], L[19], L[28], sep=', ')
hello = "안녕하세요!"
print(hello[5])
print(hello[-1])
print(L[-34], L[-26], L[-32], L[-25], L[-15], L[-6], sep=', ')
print(L[0:5], L[0:2], L[5:7], L[12:17], sep=',')
print(L[19:], L[:17], L[:], L[19:-7], sep=', ')
print(L[-22:17])
number = license_plate
print(number[-4:])
dog = "우리 강아지 이름은 초코입니다"
print(dog[11:13])
h = "20211006Rainy"
date = h[:8]
weather = h[8:]
print(date)
print(weather)
year = h[:4]
day = h[4:8]
weather = h[8:]
print(year)
print(day)
print(weather)
a = "3"
b = "4"
print(a + b)
a = 3
b = 4
print(a + b)
print("Hi"*3)
print("Hi!"*3)
print("="*80)
s1 = 'python'
s2 = 'java'
s3 = s1 + ' ' + s2 + ' '
print(s3*4)
number = 3
destination = "학교"
print("나는 사과 %d개를 먹었다. 그리고 %s에 갔다." % (number, destination))
y1 = "좋은 아침입니다!"
y2 = y1[:5] + y1[-1]
print(y2)
print("나는 사과 %d개를 먹었다." % 3)
print("나는 사과 %d개를 먹었다." % 100)
print("나는 사과 %d개를 먹었다." % 1000)
def add(a, b):
     return a + b
a = 3
b = 4
c = add(a, b)
print(c)
s = "나는 사과 %d개를 먹었다."
print(s % 1000)
num = 1000
print(s % num)
print("나는 사과 %s개를 먹었다." % "다섯")
print("나는 사과 %d개를 먹었다." % 3)
print("나는 사과 {0}개를 먹었다.".format(3))
print("나는 사과 %s개를 먹었다." % "다섯")
print("나는 사과 {0}개를 먹었다.".format("다섯"))
number = 3
print("나는 사과 {0}개를 먹었다.".format(number))
destination = "학교"
print("나는 사과 {0}개를 먹었다. 그리고 {1}에 갔다.".format(number, destination))
name1 = "김철수"
age1 =  10
name2 = "홍길동"
age2 = 13
print("이름:%s 나이:%d" % (name1, age1))
print("이름:%s 나이:%d" % (name2, age2))
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))
def minus(a, b):
    return a - b
a = 3
b = 4
print(minus(a,b))
date = "2021/09/21"
print(date[:7])
name = '홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}세입니다.")
age = 10
print(f"나는 내년이면 {age + 1}살이 된다.")
def plus(a, b):
     return a + b
def minus(a, b):
     return a - b
def multi(a, b):
     return a * b
def divi(a, b):
     return a // b

a = 6
b = 3
print(plus(a, b))
print(minus(a, b))
print(multi(a, b))
print(divi(a, b))
print(plus(b, a))
print(minus(b, a))
print(multi(b, a))
print(divi(b, a))
def hello():
     print("안녕하세요")
hello()
hello()
def hello():
     print("Hi!")
hello()
def message() :
     print("A")
     print("B")
message()
print("C")
message()
def say1(name):
     string = '안녕하세요?' + name + '님'
     return string
def say2(name): 
     string = '안녕하세요?' + name + '님'
     print(string)
name = "홍길동"
say1(name)
say2(name)
name = '홍길동'
string = say1(name)
print(string)
