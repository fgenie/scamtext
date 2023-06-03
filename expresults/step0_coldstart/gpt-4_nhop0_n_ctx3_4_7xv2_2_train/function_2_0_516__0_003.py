
import re

def is_spam(message: str) -> bool:
    # Spam word list
    spam_words = ['적중', '채팅방', '주차청', 'https://me2.kr']

    # Regular expression to match URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Check if any spam words are present in the message
    if any(word in message for word in spam_words):
        return True

    # Check if message contains more than two URLs
    if len(re.findall(url_pattern, message)) > 2:
        return True

    # If neither the spam words nor more than two URLs are present, consider the message as normal
    return False
