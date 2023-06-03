
import re

def is_spam(text):
    # Check for presence of special characters
    special_chars = re.findall('[^a-zA-Z0-9가-힣\s]', text)
    special_char_ratio = len(special_chars) / len(text)

    # Check for abnormal capitalization
    uppercase = re.findall('[A-Z]', text)
    uppercase_ratio = len(uppercase) / len(text)

    # Check for presence of numbers with text
    number_letter_combination = re.findall('[가-힣]+[\d]+', text)

    # Check for presence of urls
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    # If any of the above characteristics are found, mark the message as spam
    if special_char_ratio > 0.3 or uppercase_ratio > 0.5 or len(number_letter_combination) > 0 or len(urls) > 0:
        return True
    else:
        return False
