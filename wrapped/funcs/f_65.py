
import re

def is_spam(text):
    # Check for common spam characteristics
    spam_indicators = [
        r"(광고)",  # 'Advertisement'
        r"\d{1,2}월",  # 'Month'
        r"\d{1,2}\%",  # 'Percentage'
        r"www\.\w+\.com",  # 'URLs'
        r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
        r"무료수신거부",  # 'Free message rejection'
        r"적중",  # 'Hit'
        r"상한가",  # 'Upper limit(potentially stock market spam)'
        r"\d{1,2}만원",  # Large amounts of money
        r"금일",  # 'Today'
    ]

    # Compile the regular expressions
    spam_patterns = [re.compile(indicator) for indicator in spam_indicators]

    # Check each pattern for a match
    for pattern in spam_patterns:
        if pattern.search(text):
            return True

    # If none of the spam indicators were found, consider the message as not spam
    return False
