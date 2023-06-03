
import re

def is_spam(message):
    # Check for suspicious keywords
    spam_keywords = ["선물거래", "정확한 타점", "해외식", "증권사 매집주", "추천주", "계열사합병", "차별화 추천"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters
    special_chars = r"[!#$%&()*+,-./:;<=>?@[\]^_`{|}~]"
    special_char_count = len(re.findall(special_chars, message))

    # Check if the length of the message is beyond a certain threshold
    if len(message) > 150 and special_char_count >= 3:
        return True

    # Check for unusual links
    unusual_links = ["han.gl", "me2.kr"]
    for link in unusual_links:
        if link in message:
            return True

    # Check for suspicious phone numbers
    suspicious_phone_numbers = re.findall(r"(\d{4}[-\s]\d{4}[-\s]\d{4})", message)
    if suspicious_phone_numbers:
        return True

    return False
