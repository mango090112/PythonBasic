t = ('가위', '바위', '보')
print("""1 : 가위
2 : 바위
3 : 보""")
while True:
    data = int(input("가위, 바위, 보를 입력해주세요"))
    if data==1:
        print(t[0])
    elif data==2:
        print(t[1])
    elif data==3:
        print(t[2])
    elif data==-1:
        break
l = []
while True:
    food = input("좋아하는 음식은 무엇입니까? ")
    if food=='끝':
        break
    else:
        l.append(food)
        print(l)
a = []
while True:
    score = int(input('점수: '))
    if score == -1:
        break
    else:
        a.append(score)
        print(a)
t = ('A등급', 'B등급', 'C등급', 'D등급', 'E등급')
while True:
    score = int(input('점수: '))
    if score==-1:
        break
    elif 80 < score <= 100:
        print(t[0])
    elif 60 < score <= 80:
        print(t[1])
    elif 40 < score <= 60:
        print(t[2])
    elif 20 < score <= 40:
        print(t[3])
    elif 0 <= score <= 20:
        print(t[4])
a = []
b = []
t = ('A등급', 'B등급', 'C등급', 'D등급', 'E등급')
while True:
    score = int(input('점수: '))
    if score==-1:
        break
    elif 80 < score <= 100:
        b.append(score)
        print(b)
        a.append(t[0])
        print(a)
    elif 60 < score <= 80:
        b.append(score)
        print(b)
        a.append(t[1])
        print(a)
    elif 40 < score <= 60:
        b.append(score)
        print(b)
        a.append(t[2])
        print(a)
    elif 20 < score <= 40:
        b.append(score)
        print(b)
        a.append(t[3])
        print(a)
    elif 0 <= score <= 20:
        b.append(score)
        print(b)
        a.append(t[4])
        print(a)
