
import re


def has_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    return len(urls) > 0


def is_spam(text):
    # check if the message contains a URL
    if has_url(text):
        return True

    # check for unusual number patterns in the text
    unusual_patterns = ["[0-9]+,?[0-9]*,?[0-9]*원", "이벤트", "혜택", "무료"]
    for pattern in unusual_patterns:
        if re.search(pattern, text):
            return True

    return False

