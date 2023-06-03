def is_spam(message: str) -> bool:
    import re
    
    # Check for excessive special characters and numbers
    special_chars_and_numbers = sum([1 for char in message if not char.isalnum()])
    if special_chars_and_numbers / len(message) > 0.25:
        return True

    # Check for short urls using regex
    url_pattern = re.compile(r"https?:\/\/(?:[\w]+\.)+[\w]+\/[\w]+")
    if url_pattern.search(message):
        return True

    # Check for non-Korean or non-English characters
    non_kor_eng_chars = sum([1 for char in message if not char.isalnum() and 
                              not u'\uAC00' <= char <= u'\uD7A3' and
                              not (u'\u0041' <= char <= u'\u005A' or u'\u0061' <= char <= u'\u007A')])
    if non_kor_eng_chars / len(message) > 0.15:
        return True

    # Message is considered not-spam if none of the above conditions are met
    return False