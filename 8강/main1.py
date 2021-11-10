for number in range(1, 21, 1):
    print(number)
number = 0
while number < 20:
    number = number + 1
    print(number)
for number in range(10, 101, 1):
    print(number)
number = 9
while number < 100:
    number = number + 1
    print(number)
max = int(input())
for number in range(max+1):
    print(number)
number = 0
while number<max:
    number = number + 1
    print(number)
print("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
for number in range(min, max + 1):
    print(number)
number = min - 1
while number < max:
    number = number + 1
    print(number)
max = int(input())
for number in range(1, max + 1, 3):
    print(number)
number = 1
while number < max:
    print(number)
    number = number + 3
for number in range(1, 10):
    string = '{}x{}={}'.format(2, number, 2*number)
    print(string)
number = 5
while number > 0:
    print('*'*number)
    number = number - 1
for number in range(5, 0, -1):
    print(number*'*')
max = int(input())
for number in range(1, max + 1, 1):
    print(number*'*')
for i in range(1, 11):
    print(i)
for i in range(10):
    print(i)
for i in range(10, 0, -1):
    print(i)
for 단 in range(2, 10):
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단*number)
        print(string)
for 단 in range(2, 10):
    print('{}단 시작'.format(단))
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단*number)
        print(string)
    print('{}단 종료'.format(단))
시작단 = int(input('구구단 시작 단을 입력하세요(1~9):'))
끝단 = int(input('구구단 끝 단을 입력하세요(1~9):'))
for 단 in range(시작단, 끝단 +1):
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단*number)
        print(string)
score = int(input('학생의 점수:'))
while score > 0:
    if score >= 60:
        print('합격입니다.')
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('학생의 점수:'))
    elif score < 60:
        print('불합격입니다.')
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('학생의 점수:'))
    elif score == -1:
        score = -1
a = 0
while a < 10:
    a = a + 1
    if a % 2==0:
        continue
    print(a)
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        print('{}입니다.'.format(a))
        break
    print(a)
cap = input('한국의 수도는? : ')
a = 0
while a==0:
    if cap=='서울':
        print('정답입니다.')
        print("""그만을 입력하면 프로그램이 종료됩니다.
        """)
        cap = input('한국의 수도는? : ')
    elif cap=='그만':
        a = 1
    else:
        print("정답이 아닙니다.")
        print("""그만을 입력하면 프로그램이 종료됩니다.
        """)
        cap = input('한국의 수도는? : ')
number = int(input('입력할 수:'))
a = 0
while a == 0:
    if number % 7 == 0:
        print('7의 배수입니다.')
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        number = int(input('입력할 수:'))
    elif number == -1:
        a = 1
    else:
        print('7의 배수가 아닙니다.')
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        number = int(input('입력할 수:'))
score = int(input('점수: '))
a = 0
while a == 0:
    if score == -1:
        a = 1
    elif 81<=score<=100:
        print("A등급입니다.")
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('점수: '))
    elif 61<=score<=80:
        print("B등급입니다.")
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('점수: '))
    elif 41<=score<=60:
        print("C등급입니다.")
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('점수: '))
    elif 21<=score<=40:
        print("D등급입니다.")
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('점수: '))
    elif 0<=score<=20:
        print("E등급입니다.")
        print("""-1을 입력하면 프로그램이 종료됩니다.
        """)
        score = int(input('점수: '))
