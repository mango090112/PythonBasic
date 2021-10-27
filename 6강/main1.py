if 3<5:
    print("조건문이 True이므로 실행됩니다.")
if 3>5:
    print("조건문이 False이므로 실행되지 않습니다.")
apple = 10
if apple>=5:
    print("사과를 나누어 먹는다.")
else:
    print("사과를 혼자 먹는다.")
money = 10000
if money>=3000:
    print("택시를 타고 가라.")
else:
    print("걸어 가라.")
#rank = input('몇 등인가요?')
#if rank=='1':
   # print("TV를 보며 편안하게 쉬세요.")
#else:
 #   print('설거지 당첨!')
#number = 14
#if number%3==0:
#    print("{}는 3의 배수입니다.".format(number))
#else:
#    print("%s는 3의 배수가 아닙니다." % number)
#if number%3==0:
#    print("{}는 3의 배수입니다".format(number))
print(3 > 5)
print(3 < 5)
print(3 == 5)
print(3 != 5)
x = 4
print(1 < x <5)
print((3 == 3) and (4 != 3))

if 3<5:
    print("3은 5보다 작다.")
if 3>5:
    print("3은 5보다 크다.")
if 4<3:
    print("Hello World")
else:
    print("Hi, there.")
if True:
    print("1")
    print("2")
else:
    print("3")
    print("4")
#data = input("입력값: ")
data = 2
if int(data)%2==0:
    print("짝수")
else:
    print("홀수")
if 0<=int(data)-20<=255:
    print(int(data)-20)
elif int(data)-20<0:
    print(0)
else:
    print(255)

#grade = int(input("몇 학년인가요(1~6)?"))
grade = 3
if grade>=2 and grade<=4:
    print("햄버거를 주세요.")
else:
    print("김밥을 주세요.")
if int(data)+20 <= 255:
    print(int(data)+20)
elif int(data)+20 > 255:
    print(255)
#score = input("점수: ")
score = 23
if 81<=int(score)<=100:
    print("A등급")
elif 61<=int(score):
    print("B등급")
elif 41<=int(score):
    print("C등급")
elif 21<=int(score):
    print('D등급')
else:
    print("E등급")
#pizza = input('피자 가게가 열렸나요(예/아니요)?')
#chicken = input('치킨 가게가 열렸나요(예/아니요)?')
#김밥 = input('김밥 가게가 열렸나요(예/아니요)?')
pizza = '예'
chicken = '예'
김밥 = '예'
if pizza=='예':
    print('피자 가게로 가자')
elif chicken=='예':
    print('치킨 가게로 가자')
elif 김밥=='예':
    print('김밥 가게로 가자')
else:
    print('편의점에서 라면을 먹자')
#num1 = input("input number1: ")
#num2 = input("input number2: ")
#num3 = input("input number3: ")
num1 = 1
num2 = 2
num3 = 3
if (num1 and num2)<num3:
    print(num3)
elif num1<num2:
    print(num2)
else:
    print(num1)
주민번호 = input('주민등록번호: ')
if 주민번호[7]=='1' or 주민번호[7]=='3':
    print("남자")
elif 주민번호[7]=='2' or 주민번호[7]=='4':
    print("여자")
else:
    print("error")
def getGrade(score):
    if 81<=score<=100:
        print('grade is A')
    elif 61<=score<=80:
        print('grade is B')
    elif 41<=score<=60:
        print('grade is C')
    elif 23<=score<=40:
        print('grade is D')
    else:
        print('grade is E')
getGrade(81)
