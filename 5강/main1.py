def hello():
     print("안녕하세요")
hello()
def hi():
     print('안녕, 함수!')
print("함수 한 번 출력")
hi()
print("함수 두 번 호출")
hi()
hi()
print("함수 다섯 번 호출")
hi()
hi()
hi()
hi()
hi()
print("함수 호출 끝")
def ADD(a, b):
     result = a + b
     print(result)
ADD(10, 5)
def add(a, b):
     result = a + b
     print("{} + {} = {}".format(a, b, result))
add(10, 5)
def add_10(a):
     return a + 10
a = 12
print(add_10(a))
def print_with_smile(a):
     print(a + ":D")
print_with_smile("Hi")
def print_operation(a, b):
     add = a + b
     minus = a - b
     multi = a*b
     divi = a/b
     print(add, minus, multi, divi, sep = "/")
print_operation(3, 6)
a = "hobby"
print(a.count('b'))
name = input('당신의 이름은?')
print(name)
age = input('당신의 나이는?')
print(age)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
name = input('당신의 이름은?')
age = int(input('당신의 나이는?'))
print('당신은 ' + name + '이고, ' + str(age) + "살입니다.")
print('당신은', name, '이고', age, '살입니다.')
print('당신은 {}이고 {}살입니다.'.format(name, age))
print(name, '님은 내년에', int(age)+1, '살입니다')
print('가위 바위 보 중 하나를 내주세요> ')
mine = input()
print('mine:', mine)
date = input('오늘 날짜:')
print('오늘의 날짜는', date, '입니다.')
date = input('오늘 날짜:')
year = date[0:4]
month = date[5:7]
day = date[8:10]
print('년 :', year)
print('월 :', month)
print('일 :', day)
a = "Life is too short"
print(a.index('t'))
print(a.index('i'))
print(",".join('abcd'))
a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
b = "a:b:c:d"
print(b.split(':'))
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))
string = ' 여의도 '
print(string.strip())
string = 'Python'
print(string.upper(), string.lower(), sep = ", ")
a = "hello world"
print(a.split())
date = "2021-10-20"
print(date.split('-'))
