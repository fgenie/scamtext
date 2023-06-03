
import re

def is_spam(message: str) -> bool:
    """
    Determines if a given message is spam.

    :param message: The input message to classify.
    :return: True if the message is spam, False otherwise.
    """

    # Convert message to lowercase for easier comparison
    lower_message = message.lower()

    # Keywords and patterns that indicate spam
    spam_indicators = [
        r"\d{1,2}월",
        r"\d{1,2}일",
        r"\d{1,2}년",
        r"\d{1,2}시",
        r"\d{1,2}분",
        r"\d+만?원",
        r"지긋지긋",
        r"당일출금",
        r"지원금",
        r"비밀번호",
        r"최대[가능가소지금]",
        r"내사진",
        r"미래투자",
        r"토토사이트",
        r"대출진행",
        r"tt\.\w+",
        r"https?://(?:[a-z0-9]|[!#$%&'*+/=?^_`{|}~-])+(?:\d{4}|\d{4}-\d{4})",
        r"특별찬스",
        r"상상플러스",
        r"(?<!,)연락받아랑",
        r"예상가-?격",
        r"주말간"
    ]

    for pattern in spam_indicators:
        if re.search(pattern, lower_message):
            return True

    return False
