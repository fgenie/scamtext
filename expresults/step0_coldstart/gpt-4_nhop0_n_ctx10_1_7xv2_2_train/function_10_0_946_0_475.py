
import re

def is_spam(message):
    # Check for typical spam phrases and patterns
    spam_indicators = [
        r'\b[Vv][Ii][Pp]\b',
        r'https?://[-_a-zA-Z0-9/.]+',
        r'\b[0-9]{2,}[\.,]\?[0-9]+',
        r'\b클릭\b',
        r'\b[선정익실력매수매도시황뉴스공유]\w*\b',
        r'\b[극비장착종목명공개무료]\w*\b',
        r'\b[정식허가상한가]\w*\b',
        r'\b[확정실적상담추천가능호가]\w*\b',
        r'\b[적중단타여의도]\w*\b',
        r'\b[분석종목하락추이불안성향]\w*\b'
    ]

    # Iterate through the list of spam indicators, checking if any are present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    return False
