
import re

def is_spam(message):
    """
    This function takes a message as input and returns True if the message is a spam, False otherwise.
    It checks for common spam message patterns, such as short URLs, promotional phrases, and unusual punctuation.
    """

    # Check for presence of short URLs in the message
    short_url_patterns = [r'bit\.ly', r'goo\.gl', r'me2\.kr', r'gg\.gg', r'opcn-kakao\.com']
    if any(re.search(pattern, message) for pattern in short_url_patterns):
        return True

    # Check for promotional phrases in the message
    promo_phrases = [r'상한가확정', r'폭등예상', r'성과', r'지원금', r'거래량', r'수수료',r'무료거부']
    if any(re.search(rf'(?i){phrase}', message) for phrase in promo_phrases):
        return True

    # Check for unusual punctuation in the message
    unusual_punctuations = [
        r'\*[^\n]*\*',
        r'\-[^\n]*\-',
        r'\^[^\n]*\^',
        r'\_[^\n]*\_',
        r'◆[^\n]*◆',
        r'▲[^\n]*▲',
        r'▼[^\n]*▼',
        r'▶?[^\n]*\?'
    ]
    if any(re.search(pattern, message) for pattern in unusual_punctuations):
        return True

    return False
