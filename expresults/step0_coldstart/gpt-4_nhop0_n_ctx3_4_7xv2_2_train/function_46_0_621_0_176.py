
import re

def is_spam(text):
    # Check for common spam phrases
    spam_phrases = ["오전KC코트렐", "입장가능", "이사비지원", "IO억보증", "EE84", "금일 하루만"]
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for URL shorteners
    url_shorteners = ["bit.ly", "goo.gl", "ow.ly", "han.gl", "tinyurl.com"]
    for shortener in url_shorteners:
        if shortener.lower() in text.lower():
            return True

    # Check for large numbers or percentages in the text
    if re.search(r'\d{2,}%', text) or re.search(r'\d{4,}', text):
        return True

    # Check for special characters
    if re.search(r'[*%&$#@!^]', text):
        return True

    # If none of the above conditions are met, the message is likely not spam
    return False
