
import re

def is_spam(message: str) -> bool:

    spam_phrases = ['(광고)', '입니다', '상한가확정', '무료거부', '추천주', '결과값은', '지원받고', '적중', '최소 150%', '수익금',
                    '십만원 만들기', '소액투자', '체험반', '종목도 이어서', '상세주소', '기회를 놓치지', '만원한장 시작',
                    '수익률', '바로 입장', '신한 렌탈']

    spam_regex_patterns = [r'\bhttps?:\/\/\S+', r'\bme2\.kr\/\S+', r'\bopenkakao\.\S+', r'\bvvd\.bz\/\S+',
                           r'\[0-9]+[\u4e00-\u9fff]+']

    # Check for spam phrases
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for spam regex patterns
    for pattern in spam_regex_patterns:
        if re.search(pattern, message):
            return True

    return False
