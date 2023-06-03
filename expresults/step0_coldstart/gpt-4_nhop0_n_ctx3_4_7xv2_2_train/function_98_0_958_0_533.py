
import re

def is_spam(message):
    # Pattern for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    
    # Pattern for specialized characters that often appear in spam messages
    special_char_pattern = re.compile(r'[\\\/\[\]\-=+\|_~{}:<>?!@#$%^&\*,.;]')
    special_chars = special_char_pattern.findall(message)

    # Check for excessive use of capital letters
    capital_letters = sum(1 for char in message if char.isupper())
    excessive_caps = capital_letters / len(message) > 0.4

    # Check for excessive use of numbers
    numbers = sum(1 for char in message if char.isdigit())
    excessive_numbers = numbers / len(message) > 0.1

    # Check for typical spam words
    spam_words = ["제한", "릴", "사이트", "상품", "확실한", "폭등", "이벤트", "가입", "만원"]
    spam_word_count = sum(1 for word in spam_words if word in message)

    # If any of the conditions above are true, then the message is likely spam.
    if urls or special_chars or excessive_caps or excessive_numbers or spam_word_count > 0:
        return True
    else:
        return False
