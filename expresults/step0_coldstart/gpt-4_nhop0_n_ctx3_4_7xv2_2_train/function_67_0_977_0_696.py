def is_spam(message):
    import re
    
    # Check for common spammy phrases
    spam_phrases = ["당일기준", "조선알미늄", "기회 잡으세요", "일평균", "코드 :"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for URL patterns
    url_patterns = [
        r"https?:\/\/[^\s]+",  # HTTP and HTTPS urls
        r"(?:[a-zA-Z]*\:{0,1}[a-zA-Z]*\s?){0,1}(?:\/\s?)*[a-zA-Z0-9]*\s?\.{1}(?:(bit|me|g)?\s?(?:\.|ly)){0,2}"
    ]
    for pattern in url_patterns:
        if re.search(pattern, message):
            return True

    # Check for excessive use of special characters and numbers
    special_char_count = sum([1 for c in message if not c.isalnum()])
    num_count = sum([1 for c in message if c.isdigit()])
    if (special_char_count / len(message) > 0.15) or (num_count / len(message) > 0.2):
        return True

    return False