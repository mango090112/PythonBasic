from main1 import *

print("@@@@@")
tiger.move()

import random
for i in range(6):
    number = random.randint(1,45)
    print(number, end = ' ')

import time
current = time.ctime()
print(current)
list_cur = current.split(' ')
print(list_cur)
for t in list_cur:
    print(t)

import time
print('현재시각:', time.time())
def manyloop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')

number = int(input('숫자를 입력하세요: '))
manyloop(number)
