def is_spam(message):
    import re

    # Check for URL shorteners
    shorteners = ['bit.ly', 'goo.gl', 'tinyurl.com', 'ow.ly', 'me2.kr', 't.co', 't2m.io', 'han.gl', 'opcn-kakao.com']
    for shortener in shorteners:
        if shortener.lower() in message.lower():
            return True

    # Check for unusual number of special characters
    special_characters = ['+', '*', '_', '.']
    special_char_count = sum(message.count(char) for char in special_characters)
    if special_char_count / len(message) > 0.1:
        return True

    # Check for phone numbers
    phone_numbers = re.findall(r'\d{10,15}', message)
    if len(phone_numbers) > 0:
        return True

    # Check for too many upper case letters
    upper_case_count = sum(1 for char in message if char.isupper())
    if upper_case_count / len(message) > 0.3:
        return True

    # Check for non-korean characters
    non_korean_count = sum(1 for char in message if (ord(char) < 0xAC00 or ord(char) > 0xD7AF) and (ord(char) < 0x3130 or ord(char) > 0x318F))
    if non_korean_count / len(message) > 0.7:
        return True

    return False