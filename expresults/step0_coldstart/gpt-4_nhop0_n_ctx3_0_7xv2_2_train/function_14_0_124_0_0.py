
import re

def is_spam(message):
    # Check for short URL patterns
    short_url_patterns = [r"bit\.ly/\S+", r"vvd\.bz/\S+", r"openkakao\.at/\S+", r"t\.co/\S+"]
    for pattern in short_url_patterns:
        if re.search(pattern, message):
            return True

    # Check for money amounts and 물음표
    if re.search(r"\d{1,3}(,?\d{3})+(\s?(-|\))?/\S+)+", message) and "물음표" in message:
        return True

    # Check for specific phrases
    spam_phrases = ["신 청 하 신", "하루 20분!", "힘든시기 이곳에서 해결", "당첨 5Dg88"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Return False if none of the above conditions were met
    return False
