
import re

def is_spam(message):
    # Define the RegExp patterns for URLs and email addresses.
    url_pattern = r'(http|https)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Count the number of URLs and email addresses in the message
    url_count = len(re.findall(url_pattern, message))
    email_count = len(re.findall(email_pattern, message))

    # Check if the message contains characters that are not in Korean or English
    non_korean_english_chars = '[^ 가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9\s.,?!\-_%@]'
    non_korean_english_count = len(re.findall(non_korean_english_chars, message))

    # Determine if the message is spam based on the counts
    if url_count > 0 or email_count > 0 or non_korean_english_count > 0:
        return True
    else:
        return False
