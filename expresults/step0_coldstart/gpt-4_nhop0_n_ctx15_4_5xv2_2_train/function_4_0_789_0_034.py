import re

def is_spam(text: str) -> bool:
    # Basic spam indicators
    spam_words = ["상한가", "추천", "vip", "관심종목", "명가", "수익률", "비번", "비밀번호", "차트", "투자"] 
    text_lower = text.lower()

    for word in spam_words:
        if word in text_lower:
            return True

    # Check for URLs
    url_regex = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    urls = re.findall(url_regex, text)
    if len(urls) > 0:
        return True

    # Check for unusual patterns
    unusual_patterns = ["[0-9]+%[\\+\\-↑]", "key:[0-9]+", "코드번호 [0-9]+"]
    for pattern in unusual_patterns:
        if re.search(pattern, text):
            return True

    # Check for sequences of numbers and characters combined
    sequences = re.findall("([0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]+)", text)
    if len(sequences) > 1:
        return True

    return False