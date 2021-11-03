hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {}번 찍었습니다.".format(hit))
number = 0
while number < 5:
    number = number + 1
    print(number)
hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어갔습니다.")
hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어갔습니다.")
    elif hit == 8:
        print("나무가 곧 넘어갈것 같습니다.")
    elif hit <= 3:
        print('나무가 꿈쩍도 하지 않습니다.')
    elif hit == 6:
        print('나무가 조금씩 흔들리고 있습니다.')
prompt = '''
100을 입력하면 종료가 되는 프로그램입니다.
100. 종료
Enter number:'''
number = 0
while number != 100:
    print(prompt)
    number = int(input())
a = 2
while 2 <= a < 6:
    a = a + 1
    print(a)
a = 2
while 2 <= a < 6:
    a = a + 1
    print(a)
    print("-------")    
a = 0
while a < 1000:
    a = a + 1
    print(a)
number = 0
while number < 10:
    number = number + 1
    print(number)
number = 1
while number <= 10:
    print(number)
    number = number + 1
number = 0
while number < 100:
    number = number + 1
    print(number)
number = 1
while number <= 100:
    print(number)
    number = number + 1
number = 0
max = int(input("입력할 수:"))
while number < max:
    number = number + 1
    print(number)
#while 3<5:
    #print('3은 5보다 작다.')
if 3<5:
    print("3은 5보다 작다.")
print("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
while min<=max:
    print(min)
    min = min + 1
#while True:
    #print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
number = 0
while number<=1000:
    number = number + 1
    if number%3==0:
        print(number)
num = 0
while num<=9:
    num = num + 1
    if num%2==1:
        print("3x{0}={1}".format(num,num*3))
a = 0
b = 0
while a < 10:
    a = a + 1
    b = b + a
print(b)
a = 0
b = 0
while a < 10:
    a = a + 1
    if a%2==1:
        b = b + a
print(b)
a = 0
b = 1
while a < 10:
    a = a + 1
    b = b * a
print(b)
a = 0
while a < 5:
    a = a + 1
    print('*'*a)
for number in range(1, 21, 1):
    print(number)
for number in range(1, 101, 1):
    print(number)
max = int(input('입력할 수:'))
for number in range(0, max+1, 1):
    print(number)
for number in range(1, 10):
    string = '{}x{}={}'.format(9, number, 9*number)
    print(string)
단 = int(input('구구단을 출력합니다. 몇 단인지 입력해주세요.'))
for number in range(1, 10):
    string = '{}x{}={}'.format(단, number, 단*number)
    print(string)
for number in range(1, 11, 1):
    print(number)
for number in range(1, 1001):
    print(number)
