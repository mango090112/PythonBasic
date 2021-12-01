import random
com = random.randint(0, 100)
print('0~100까지의 숫자를 입력하세요. 포기하고 싶다면 -1을 입력하세요 ')
count = 0
while True:
    count = count + 1
    print('{}번째 도전!!'.format(count))
    user = int(input('''당신의 선택은 ? 
'''))
    if user > com:
        print('정답보다 크네요')
    elif user==-1:
        print('정답은 {}..!'.format(com))
        break
    elif user < com:
        print('정답보다 작네요')
    else:
        print('정답입니다')
        break
com1 = random.randint(0, 100)
com2 = random.randint(0,100)
a = com1 + com2
if com1-com2 < 0:
    b = com2-com1
else:
    b = com1-com2
print("임의의 두 숫자가 주어집니다. 두 수를 더한 값을 구하세요")
while True:
    user = int(input('당신의 답은 ? '))
    if user < a:
        print('정답보다 작네요')
    elif user > a:
        print('정답보다 크네요')
    else:
        print('정답입니다')
        break
print("이번에는 두 수의 차를 구해보세요")
while True:
    user = int(input('당신의 답은 ? '))
    if user < b:
        print('정답보다 작네요')
    elif user > b:
        print('정답보다 크네요')
    else:
        print('정답입니다')
        break
