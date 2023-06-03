
import re

def is_spam(message):
    # Detect if message contains a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    contains_url = bool(url_pattern.search(message))

    # Detect if message contains korean
    korean_pattern = re.compile(r'[\uac00-\ud7a3]')
    contains_korean = bool(korean_pattern.search(message))

    # Detect if message has special characters
    special_characters_pattern = re.compile(r'[-_!@$%^&*+=}{\[\]|\\:;"\'<>,.?/]')
    contains_special_characters = bool(special_characters_pattern.search(message))

    # Check for spam keywords
    spam_keywords = ["정회원방", "안내", "악성광고", "명가로와주세요", "코드", "대충", "주세요"]
    contains_spam_keywords = any(keyword in message for keyword in spam_keywords)

    # Classify message as spam if it contains a URL, contains
    # korean, or contains spam keywords
    if contains_url and contains_korean and (contains_special_characters or contains_spam_keywords):
        return True
    else:
        return False
