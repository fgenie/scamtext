def is_spam(message: str) -> bool:
    import re

    # Check for typical spam words/phrases
    spam_words = ['(광고)', '당첨 되셨습니다', '총 수익', '무료수신거부', '증권사 매집주', '경제야 놀자 TV']
    if any(word in message for word in spam_words):
        return True

    # Check for suspicious URLs
    url_pattern = re.compile(r'(http|https)://[^\s]*')
    if url_pattern.search(message):
        return True

    # Check for suspicious message patterns
    pattern = re.compile(r'(\b\d{1,2} 부\b)|(\d{1,3},\d{3} 수익)')
    if pattern.search(message):
        return True

    # If none of the above, classify as normal message
    return False