def is_spam(message):
    import re

    # Check for common spam keywords
    spam_keywords = ['(광고)', '100전', '상한가확정', '실. 제. 성. 과.', 'VIP', '수익', 'free']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters
    special_chars = set("{}()[].!$@#%^&*-=:/,|;<>?+")
    special_count = sum(1 for c in message if c in special_chars)
    if special_count / len(message) > 0.05:
        return True

    # Check for presence of URLs
    url_pattern = re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9_%]*)\b\.\w{2,4}')
    if url_pattern.search(message):
        return True

    # Check for phone numbers
    phone_number_pattern = re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?=\s?[0-9]))|#)?\s*?(\d{1,}\d{1,})\s*(?:\|\d{1,}\d{1,})*>?', re.ASCII)
    if phone_number_pattern.search(message):
        return True

    return False