def is_spam(message: str) -> bool:
    import re

    # Check for URLs with suspicious domain extensions
    suspicious_url_pattern = re.compile(r'https?://\S*\.(kr|io)\b')
    if suspicious_url_pattern.search(message):
        return True

    # Check for presence of stock-related words and percentages
    stock_pattern = re.compile(r'(\d{1,2}%\W*↑)|((\s|-)*주차)')
    if stock_pattern.search(message):
        return True

    # Check for presence of VIP or 신청 in the message
    vip_or_signup_pattern = re.compile(r'(VIP|신청)')
    if vip_or_signup_pattern.search(message):
        return True

    # If none of the conditions above are met, classify the message as normal
    return False