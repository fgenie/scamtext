def is_spam(text):
    import re

    # Check for common spam keywords
    spam_keywords = ['공시발표', '투자', '발표예정', '체험반', '단독입수', '폭등확정']
    keyword_count = sum(word in text for word in spam_keywords)
    if keyword_count > 1:
        return True

    # Check for URL shorteners
    url_shorteners = ['me2.kr', 'bit.ly', 'goo.gl']
    for shortener in url_shorteners:
        if shortener in text:
            return True

    # Check for the presence of URLs followed by short texts or non-alphabetic characters
    url_pattern = re.compile(r'https?://\S+\b')
    if url_pattern.search(text) and len(re.sub(url_pattern, '', text).strip()) < 15:
        return True

    # If none of the above conditions are met, the message is considered not spam
    return False