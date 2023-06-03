
import re

def is_spam(text: str) -> bool:
    # Check for patterns observed in spam messages
    spam_patterns = [
        r"\d{1,2}%",  # Percentage discounts
        r"코드[:\:]?\w*",
        r"무료거부",  # Unsubscribe keyword in Korean
        r"(http(s)?://)?(bit\.ly|me2\.kr|vo\.la|dokdo\.in|tdeal\.kr|"\
        "openkak(talk)?\.at|kakaos?\.co|buly\.kr|(vvd\.bz))\/\S*",  # Spam URL shorteners
        r"=BBQ\+피자\+활쿱",  # Spam message
        r"(광고)",  # Advertising indicator
    ]

    # Combine all spam patterns into a single regex pattern
    spam_pattern_re = re.compile("|".join(spam_patterns), re.IGNORECASE)

    return bool(spam_pattern_re.search(text))

