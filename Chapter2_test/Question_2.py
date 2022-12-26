# 서기 연도가 인수로 주어질 때, 조선시대 왕조의 계보로 변환하여 출력

year = int(input('년도를 입력하세요'))

def chosun(year):
    if year >= 1392 and year < 1398:
        print('태조 '+ str(year - 1392 + 1) + '년')
    elif year >= 1398 and year < 1400:
        print('정종 ' + str(year - 1398 + 1) + '년')
    elif year >= 1400 and year < 1418:
        print('태종 ' + str(year - 1400 + 1) + '년')
    elif year >= 1418 and year < 1450:
        print('세종 ' + str(year - 1418 + 1) + '년')
    elif year == 1450:
        print('문종 1년')
    else:
        print('아직 등록하지 않았습니다.')

chosun(year)