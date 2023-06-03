
import re

def is_spam(message: str) -> bool:
    # Check for common spam phrases
    spam_phrases = [
        "축하드립니다",
        "안전하고 확률",
        "정보방",
        "차별화된 정보",
        "호재성 공시",
        "알아두세요",
        "사라질예정",
        "무료거부",
        "광고",
        "지금 확인",
        "지금 사야",
        "지원금",
        "참여하새요",
        "비밀번호",
        "다음주 종목",
        "예정",
        "세력 정보주"
    ]

    # Check for presence of URLs
    url_pattern = re.compile(r'(?:www|https?://\S+)')

    # Check for excessive usage of special characters
    special_char_pattern = re.compile(r'[\*\!\"\%\(\)\\\'\+\<\-\>\@\[\]^_`{|}~\(\)]{2,}')

    # Check for presence of number sequences
    number_pattern = re.compile(r'\d{2,}')

    message = message.lower()

    # Check for spam phrases
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for presence of URLs
    if url_pattern.search(message) is not None:
        return True

    # Check for excessive usage of special characters
    if special_char_pattern.search(message) is not None:
        return True

    # Check for presence of number sequences
    if number_pattern.search(message) is not None:
        return True

    return False
