list = [1, 5, 3, 6]
print(list)
print(list[1])
print(list[-3])
print(list[2:4])
print(list[2:])
print(list[:2])
length = len(list)
print(length)
list = ['안녕', '친구들', '만나서', '반가워']
print(list[3])
과목 = ['국어', '수학', '영어', '과학']
print(과목)
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다.'.format(first_color))
last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다.'.format(last_color))
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
List = [1, 5, 3, 6]
List[0] = 10
print(List)
List[0:2] = [10, 50]
print(List)
list = [1, 5, 3, 6]
list.append(8)
print(list)
list = [1, 5, 3, 6]
list.insert(2, 4)
print(list)
list = [1, 5, 3, 6]
del list[0]
print(list)
list = [1, 5, 3, 6]
list.remove(3)
print(list)
list = [1, 5, 3, 6, 3]
list.remove(3)
print(list)
list = [1, 2, 3]
list.append(4)
print(list)
list = [1, 2, 3, 5]
list.insert(3, 4)
print(list)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
list = [1, 2, 3]
del list[1]
print(list)
list = [1, 2, 3]
list.remove(2)
print(list)
list = [1, 2, 3]
list[1] = 10
print(list)
title = """
구구단 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료"""
print(title)
number = 0
while number==0:
    a = int(input())
    if a==3:
        number=1
    elif a==1:
        for 단 in range(1,10,1):
            if 단%2==1:
                for b in range(1,10,1):
                    print('{}x{}={}'.format(단, b, 단*b))
    elif a==2:
        for 단 in range(1, 10, 1):
            if 단%2==0:
                for c in range(1,10,1):
                    print('{}x{}={}'.format(단, c, 단*c))
    else:
        number=0
tuple = (1, 2, 3, 4, 5)
print(tuple)
tuple = 1, 2, 3, 4, 5
print(tuple)
t1 = (1, 2, 'a', 'b')
#del t1[0]
#t1[0] = 'c'
print(t1[0])
print(t1[1:])
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
print(len(t1))
음식 = ('햄버거', '피자', '감자탕', '김밥', '타코', '탕수육')
print(음식)
rainbow = ('빨강', '주황', '노랑', '초록', '파랑', '남색', '보라')
first_color = rainbow[0]
print('무지개의 마지막 색은 {}이다.'.format(first_color))
last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다.'.format(last_color))
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t*10)
t2 = t*10
print(len(t2))
my_variable = []
print(my_variable)
movie_rank = ['아바타', '어벤져스', '타이타닉', '명량', '겨울왕국2']
del movie_rank[1]
print(movie_rank)
movie_rank = ['아바타', '어벤져스', '타이타닉', '명량', '겨울왕국2']
movie_rank.remove('어벤져스')
print(movie_rank)
movie_rank = ['아바타', '어벤져스', '타이타닉', '명량', '겨울왕국2']
movie_rank.insert(4, '겨울왕국')
print(movie_rank)
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","Go","C#"]
langs = lang1+lang2
print(langs)
my_variable = ()
print(my_variable)
movie_rank = ('아바타','어벤져스','타이타닉','명량','겨울왕국')
print(movie_rank)
t = (1, 2, 3)
#t[0] = 'a'
print("""
1-주먹
2-가위
3-보""")
data = int(input("1, 2, 3을 입력해주세요."))
t = ('주먹', '가위', '보')
if data==1:
    print(t[0])
elif data==2:
    print(t[1])
elif data==3:
    print(t[2])
