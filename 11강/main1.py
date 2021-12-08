dic = {}
print(dic)
dic = {'이름': '전예서', '나이': 13, '성별': '여성', '생일':'1월 12일'}
print(dic)
ice = {'메로나':1000, '비비빅':1200, '빵빠레': 1800}
print(ice)
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)
print('메로나 가격:', ice['메로나'])
ice['메로나'] = 1300
print(ice)
del ice['메로나']
print(ice)
ice = {'메로나':[1000,2], '비비빅':[1200,3], '빵빠레':[1800,100]}
print(ice)
print(ice['메로나'][0], '원')
print(ice['메로나'][1], '개')
ice['월드콘'] = [500,7]
print(ice)
dic = {}
print(dic)
days = {'1월':31,'2월':28,'3월':31,'4월':30,'5월':31,'6월':30,'7월':31,'8월':31,'9월':30,'10월':31,'11월':30,'12월':31}
print(days)
days['2월'] = 29
print(days)
days['13월'] = 30
print(days)
del days['13월']
print(days)
data = int(input('숫자 입력 : '))
korean = {0 : '영', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구'}
print(korean[data])
def korean_number(num):
    korean = {0 : '영', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구'}
    a = korean[num]
    return a
num = int(input('숫자 입력 : '))
print(korean_number(num))
while True:
    num = int(input('숫자 입력 : '))
    if num==-1:
        break
    else:
        print(korean_number(num))
구슬집합 = set(['파란구슬', '노란구슬', '파란구슬', '빨간구슬'])
print(구슬집합)
print(구슬집합)
print(구슬집합)
print(구슬집합)
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s = set(a)
print(s)
s = set("Hello")
print(s)
A = {2, 1, 3, 5, 7}
B = {3, 4, 1, 6}
print(A & B)
print(A | B)
print(A - B)
print(B - A)
string = '안녕하세요'
for 변수 in string:
    print(변수)
list = ['리', '스', '트', 1, 2, 3]
for 변수 in list:
    print(변수)
tuple = ('튜', '플', 4, 5, 6)
for 변수 in tuple:
    print(변수)
과일 = ['사과', '귤', '수박']
for 변수 in 과일:
    print(변수)
for a in [10, 20, 30]:
    print(a)
for a in [10, 20, 30]:
    print(a)
    print("-------")
리스트 = ['김밥', '라면', '튀김']
for a in 리스트:
    print('오늘의 메뉴 :', a)
for a in 리스트:
    print(a[0])
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0:
        print(변수)
튜플 = (3, 100, 23, 44, 103, 28, 99, 65, 63, 3333)
for 변수 in 튜플:
    if 변수%3==0:
        print(변수)
A = {2, 1, 3, 5, 7, 10, 100, 283}
B = {3, 4, 1, 6, 22, 100, 302}
print(A & B)
print(A | B)
print(A - B)
print(B - A)
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수)
for 변수 in 리스트:
    print(변수, len(변수))
