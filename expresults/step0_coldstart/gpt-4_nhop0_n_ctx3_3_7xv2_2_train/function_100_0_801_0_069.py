
import re

def is_spam(message):
    # Check for common spam phrases and patterns
    spam_phrases = [
        "지급",
        "수수료",
        "지원받고",
        "지원방",
        "입장코드",
        "조합",
        "투자",
        "선물",
        "수익금",
        "정보/혜택",
        "안정적인",
        "작성",
        "현명한 선택",
        "현명한 투자",
        "출금",
        "사랑하는 사람이라서",
        r"\d+%"
    ]

    # Compile a regex of spam phrases and patterns
    spam_pattern = "|".join(spam_phrases)
    spam_regex = re.compile(spam_pattern)

    # Check if message matches spam pattern
    if spam_regex.search(message):
        return True

    # Check for suspicious URLs
    url_pattern = r"https?://[\w\.-]+"
    url_regex = re.compile(url_pattern)

    # Check if message contains a URL
    if url_regex.search(message):
        return True

    return False
