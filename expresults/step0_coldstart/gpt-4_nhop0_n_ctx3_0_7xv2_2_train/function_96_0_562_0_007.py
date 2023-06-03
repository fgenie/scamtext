
import re

def is_spam(message):
    short_link_patterns = ['me2\.kr', 'kakaotalk\.it', 'bit\.ly']
    spam_keywords = ['신청하신', '입장', '해.외.선.물.', '강의', '일타강사진', '교육', '선착모집', '비밀번호', '축하합니다!', '체험반']

    for pattern in short_link_patterns:
        if re.search(pattern, message):
            return True

    spam_keyword_count = sum([1 for keyword in spam_keywords if keyword in message])

    if spam_keyword_count >= 2:
        return True

    return False
