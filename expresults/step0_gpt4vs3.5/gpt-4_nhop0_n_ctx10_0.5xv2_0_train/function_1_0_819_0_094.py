
import re

def is_spam(message):
    # Check for multiple exclamation marks or URLs
    if re.search(r"((!{2,})|((https?:\/\/|bit\.ly|me2\.kr|kakaosa\.co\.kr|han\.gl)[^\s]+))", message):
        return True

    # Check for excessive use of numbers and special characters
    if re.search(r"([0-9]{2,}[\s\,\.]{1,}[0-9]{2,})", message) or re.search(r"[*_\-]{3,}", message):
        return True

    # Check for words associated with spam
    spam_words = ["상승", "상한가", "주식", "종목", "수익", "바로가기", "체험반", "선별", "비결"]
    for word in spam_words:
        if word in message:
            return True

    # If none of the spam conditions are met, return False
    return False
