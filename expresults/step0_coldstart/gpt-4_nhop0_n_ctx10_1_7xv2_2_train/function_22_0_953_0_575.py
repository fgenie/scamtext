
import re

def is_spam(message: str) -> bool:
    # Checking for common spam characteristics:
    # 1. Contains a URL
    url_pattern = r'(https?://\S+|www\.\S+)'
    if re.findall(url_pattern, message):
        return True

    # 2. Has excessive digits or special characters (more than 20% of the message)
    non_alpha = len([ch for ch in message if not ch.isalnum()])
    if non_alpha > 0.2 * len(message):
        return True

    # 3. Contains specific spam-related keywords
    spam_keywords = ['추천주', '적중', '상한가', '테마주', '수익', '코드번호', '온라인', '게임', '계열', 'VIP', '포인트', '텔레그램']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the spam characteristics found, we assume it's not a spam
    return False
