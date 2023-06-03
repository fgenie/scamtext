def is_spam(text):
    import re
    
    # Check for keywords like "광고", "무료", "단기", "장기", "추천주", "현황", "패키지", "롯", "원", "연후"
    spam_keywords = ["광고", "무료", "단기", "장기", "추천주", "현황", "패키지", "롯", "원", "연후"]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for unusual urls or short links
    url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    short_url_regex = re.compile(r'(?i)(?:https?://)?(?:www)?\w+\.(?:\w{2,8}[/.]?)\w{0,4}(/[a-zA-Z0-9#=_\-\?& \%\.]+)?')
    if url_regex.search(text) or short_url_regex.search(text):
        return True

    # Check for phone numbers with 4-4-4 or 3-4-4 format (e.g. 010-1234-5678 or 02-1234-5678)
    phone_number_regex = re.compile(r'(\d{2,4}-\d{4}-\d{4})')
    if phone_number_regex.search(text):
        return True

    # If none of the spam patterns is found, return False
    return False