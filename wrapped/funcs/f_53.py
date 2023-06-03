
import re

def is_spam(message):
    """
    This function takes a message and returns True if it's a spam message and False otherwise.
    """
    # check for spam keywords
    spam_keywords = ["(광고)", "수익", "무료", "VIP", "안전", "건", "신입", "정보", "트레이딩", "대표님", "추천", "공개", "체험반", "보유종목", "프로", "실력", "초보", "개인정보",
                     "비밀번호", "복구", "님", "혜택"]

    # check for URL patterns
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # check for phone numbers
    phone_pattern = re.compile(r'(\d{2,4}-\d{3,4}-\d{3,4})|(\(\d{2,4}\)\d{3,4}-\d{3,4})')

    # check if message contains any spam keywords
    if any(keyword in message for keyword in spam_keywords):
        return True

    # check if message contains URLs
    if url_pattern.search(message):
        return True

    # check if message contains phone numbers
    if phone_pattern.search(message):
        return True

    # if message passed all the checks, it is not spam
    return False
