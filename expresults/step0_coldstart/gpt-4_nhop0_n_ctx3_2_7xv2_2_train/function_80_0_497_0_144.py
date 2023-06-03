
import re

def is_spam(message):
    # Check for suspicious phrases commonly found in spam messages
    phrases = ["최고급 정보", "bit.ly", "확인", "상상도 못한", "한번만", "놓치지마세요",
               "1일만에", "상승 확정", "익절 가능", "공개 오픈초대", "상한가", "특별한 기회",
               "무료", "폭등", "목표달성"]

    for phrase in phrases:
        if phrase in message:
            return True

    # Check for unusual repetitive patterns
    spam_pattern = re.compile(r'(.)\1{2,}')
    if len(spam_pattern.findall(message)) > 0:
        return True

    # Check for long URLs
    url_pattern = re.compile(r'(https?://\S+)')
    urls_found = re.findall(url_pattern, message)
    for url in urls_found:
        if len(url) > 20:
            return True

    # If none of the conditions are met, it's considered not spam
    return False
