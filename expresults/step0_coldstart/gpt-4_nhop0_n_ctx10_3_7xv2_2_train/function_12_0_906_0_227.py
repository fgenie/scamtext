
import re

def is_spam(message: str) -> bool:
    # Check for consecutive special characters or excessive white spaces
    special_chars_consecutive = re.compile(r'[!@#$%^&*(){}\[\]:;.,/?-_<>+=`~]{2,}')
    excessive_white_spaces = re.compile(r'\s{3,}')
    if special_chars_consecutive.search(message) or excessive_white_spaces.search(message):
        return True

    # Check for non-standard characters and meaningless words
    non_standard_chars = re.compile(r'[^\w\d\s.,!?<>_\-+@%/]', flags=re.UNICODE)
    if non_standard_chars.search(message):
        return True

    # Check for excessive capital letters
    num_uppercase = sum(letter.isupper() for letter in message)
    if num_uppercase / len(message) > 0.5:
        return True

    # Check for typical spam phrases
    spam_phrases = ['충전이벤트','적립금','모집', '시작','투자','오픈','정치세력','카톡방']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # If none of the above conditions are met, it's considered a normal message
    return False
