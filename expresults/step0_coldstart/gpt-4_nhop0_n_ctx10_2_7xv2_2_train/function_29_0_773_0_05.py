import re

def is_spam(message):
    spam_indicators = [
        r'\d+%',
        r'[가-힣]+\s*:\s*[a-zA-Z0-9\s]*\s*-\s*[\s\S]*',
        r'[▶★]+',
        r'http[^\s]+(\.|\/)kr[^/\s]*',
        r'\d+\s*[+]\s*\d+',
        r'[\d,]+\s*[원]',
        r'\d+천원',
        r'￣+',
        r'☆',
        r'[≣≤≥⊃]',
        r'(무료|가능한)\s*[%:%=]',
        r'(기업세력|현직국회의원|신규정보)',
        r'(준비물|종료되었습니다|광 의)\:',
        r'주식은',
        r'(목표가|현재가)\:',
        r'(입장코드|비밀번호)\:',
        r'추천',
        r'(광고)',
        r'(다음종목)\s*[▼↑]',
        r'\(스팸\)'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    return False