def is_spam(message):
    import re

    # Check for any suspicious URLs
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if len(urls) > 0:
        for url in urls:
            if ".gl/" in url or ".ly/" in url or "me2.kr" in url:
                return True

    # Check for any phone numbers
    phone_numbers = re.findall(r'(\d{3})\D{0,3}(\d{3}|\d{4})\D{0,3}(\d{4})', message)
    if len(phone_numbers) > 0:
        return True

    # Check for any suspicious email addresses
    email_addresses = re.findall('[\w\.-]+@[\w\.-]+', message)
    if len(email_addresses) > 0:
        for email in email_addresses:
            if "noreply@" in email.lower():
                return True

    # Check for any suspicious phrases or words
    bad_words = ["광고", "지원금", "당일 출금", "선물", "최소", "종목상담", "추천", "공개성공"]
    for bad_word in bad_words:
        if bad_word in message:
            return True

    return False