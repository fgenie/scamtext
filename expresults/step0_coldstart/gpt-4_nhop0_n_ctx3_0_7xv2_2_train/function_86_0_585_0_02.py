import re

def is_spam(message):
    spam_indicators = [
        '정회원',
        'VIP',
        '부터 시작',
        'https://me2.kr',
        '타점/분석',
        '공개',
        '시황',
        '입증',
        'C제약',
        '상한가',
        '오파스넷',
        '추천 수익',
        '공개',
        '추천주',
        '긴급입수정보'
    ]

    normal_indicators = [
        '전화드렸는데',
        '문자 남깁니다',
        '업무미팅건',
        '운지않을까',
        '예금을 송금하다',
        '반출금지걸려있네요'
    ]

    spam_counter = 0
    normal_counter = 0

    for indicator in spam_indicators:
        if indicator in message:
            spam_counter += 1

    for indicator in normal_indicators:
        if indicator in message:
            normal_counter += 1

    if spam_counter > normal_counter:
        return True
    else:
        return False