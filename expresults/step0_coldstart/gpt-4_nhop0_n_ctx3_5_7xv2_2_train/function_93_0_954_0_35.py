def is_spam(message: str) -> bool:
    import re

    # Check for unusual character patterns (e.g. mixed case or special characters)
    if re.search(r'[가-힣]\s*[A-Za-z0-9]', message) or re.search(r'[A-Za-z0-9]\s*[가-힣]', message):
        return True

    # Check for presence of URLs
    if re.search(r'(http|https)://[A-Za-z0-9./]+', message) or re.search(r'bit\.ly/[A-Za-z0-9./]+', message):
        return True

    # Check for excessive use of numbers (e.g. large amounts of money)
    if len(re.findall(r'\d{4,}', message)) > 1:
        return True

    # Check for usage of specific keywords
    spam_keywords = ['적립금', '당', '-', 'I', '.', 'r']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for short links
    if re.search(r'[a-z0-9]+(\.[a-z]+/)', message):
        return True

    # Check for specific word patterns
    if re.search(r'\s{2,}', message):
        return True

    return False