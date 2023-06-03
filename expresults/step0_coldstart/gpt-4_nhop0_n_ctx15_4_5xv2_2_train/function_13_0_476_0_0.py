def is_spam(text):
    import re
    
    spam_indicators = [
        '상한가',
        '무료거부',
        '수익률',
        '비트코인',
        '투자',
        '예정',
        '단독',
        '체험',
        '연소득',
        '선물거래',
        '시초가',
        '확률',
        '실적',
        '텔레그램',
        '마감'
    ]

    if any(indicator in text for indicator in spam_indicators) and len(re.findall('\W',text))/len(text) > 0.1:
        return True
    else:
        return False