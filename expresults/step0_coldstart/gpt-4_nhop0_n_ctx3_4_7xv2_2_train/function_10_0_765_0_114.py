
import re

def is_spam(message):
    # Check for common spam keywords
    spam_keywords = ["입금", "출금", "혜택", "체험반", "공시발표", "시작"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for links
    url_pattern = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
    if url_pattern.search(message):
        return True

    # Check for consecutive repeated characters
    for i in range(len(message) - 2):
        if message[i] == message[i + 1] and message[i + 1] == message[i + 2]:
            return True

    # If none of the conditions match, it's not spam
    return False
