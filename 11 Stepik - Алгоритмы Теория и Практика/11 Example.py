2.1 - инверсий нет
res[] = {1, }
b[] = {/ , 3, 4, 7}
c[] = {2, 5, 6, 8}

2.2 - инверсия - так как берем из C
res[] = {1,2 }
b[] = {/ , 3, 4, 7}//здесь вышла единица
c[] = {/, 5, 6, 8}//здесь вышла двойка

2.3 - нет
res[] = {1,2,3}
b[] = {/ , /, 4, 7}//Вышли единица и тройка
c[] = {/, 5, 6, 8}//Вышла двойка

2.4 - нет
res[] = {1,2,3,4}
b[] = {/ , /, /, 7}//Вышли единица, тройка, четвёрка
c[] = {/, 5, 6, 8}//Вышла двойка

2.5 - инверсия
res[] = {1,2,3,4,5}
b[] = {/ , /, /, 7}//Вышли единица, тройка, четвёрка
c[] = {/, /, 6, 8}//Вышла двойка


6
10 8 6 2 4 5
answer is 12
----------
6
1 9 8 1 4 1
answer is 8
----------
6
6 5 8 6 0 4
answer is 10
----------
6
6 2 3 7 5 8
answer is 4
----------
6
6 4 5 0 0 2
answer is 11
----------
6
8 9 10 7 4 0
answer is 12
----------
6
10 9 3 8 3 10
answer is 8
----------
6
9 10 9 5 7 7
answer is 10
----------
6
9 5 8 9 4 10
answer is 6
----------
6
5 7 0 2 2 0
answer is 10