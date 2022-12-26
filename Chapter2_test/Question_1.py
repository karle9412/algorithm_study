# 1950년에서 2050년 사이의 윤년을 출력
full_year = [i for i in range(1950, 2051)]

for i in full_year:
    if i % 4 == 0:
        if i % 100 != 0 or i % 400 == 0:
            print(i, end=' ')

