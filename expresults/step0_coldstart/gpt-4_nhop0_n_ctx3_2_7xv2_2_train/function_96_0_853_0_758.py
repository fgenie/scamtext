def is_spam(text):
    import re
    
    # Check for special characters
    num_special_chars = len(re.findall(r'[!@#$%^&*()_+{}|:"<>?/`~,.;[\]]', text))
    if num_special_chars > 5:
        return True
    
    # Check for multiple white spaces between words
    num_words = len(re.findall(r'\S+', text))
    if num_words < 5 or num_words > 50:
        return True

    # Check for URL patterns
    url_patterns = [r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*´`]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                    r'(?:www.|me2\.kr/|s\s|i\s\sl\s102.com)',
                    r'(bit.ly/|bit.do/|tinyurl.com/|me2.kr/|ow.ly/)']
    for pattern in url_patterns:
        if re.search(pattern, text):
            return True

    # Check for capitalization ratio
    num_uppercase_letters = len(re.findall(r'[A-Z]', text))
    num_lowercase_letters = len(re.findall(r'[a-z]', text))
    if num_uppercase_letters > 0 and num_lowercase_letters > 0:
        cap_ratio = float(num_uppercase_letters) / float(num_lowercase_letters)
        if cap_ratio > 0.7:
            return True

    return False