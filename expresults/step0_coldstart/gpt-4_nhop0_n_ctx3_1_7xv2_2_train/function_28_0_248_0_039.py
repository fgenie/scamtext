
import re

def is_spam(message):
    # Check for common spam phrases
    spam_phrases = [
        "당첨 되셨습니다",
        "수익",
        "최근 .* 매매 성과",
        "투자계획",
        "투자 대회",
        "단체방 관망하기",
        "종목확인",
        "종목/편입가"
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    # Check for consecutive urls
    url_pattern = r"https?://\S+|www\.\S+"
    urls = re.findall(url_pattern, message)
    if len(urls) > 1:
        return True

    # Check for unusual character repetitions
    repetition_pattern = r"(.)\1{3,}"
    repetitions = re.findall(repetition_pattern, message)
    if len(repetitions) > 0:
        return True

    # If none of the spam checks matched, consider it a normal message
    return False
