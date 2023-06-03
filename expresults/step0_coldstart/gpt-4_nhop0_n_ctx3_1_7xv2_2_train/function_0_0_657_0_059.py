
import re

def is_spam(message):
    # Check for common spam phrases
    spam_phrases = ['축하드립니다', '다음타자', '내일 발표', '엠바고', '최소3연상', '미리확인',
                    '긴급입수정보', '상한가 확정', '본격진출', '상장스타트업', '계열사합병',
                    'FROG', '무료체험반', '8,930.000원 달 성', '15만원만 준비하세요']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    match = re.search(url_pattern, message)

    if match:
        return True

    # Check for excessive punctuation
    if '!' in message:
        if message.count('!') > 3:
            return True

    if '-' in message:
        if message.count('-') > 5:
            return True

    # If none of the spam conditions are met, it is not spam
    return False
