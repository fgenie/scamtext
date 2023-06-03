
import re

def is_spam(message: str) -> bool:
    # Check for a high number of non-alphanumeric characters
    non_alnum_percent = len(re.findall(r'\W', message)) / len(message)
    if non_alnum_percent > 0.5:
        return True

    # Check for suspicious URL patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if urls:
        short_url_pattern = re.compile(r'(me2|bit)\.(?:[a-z]{2,})')
        for url in urls:
            if short_url_pattern.search(url):
                return True

    # Check for currency amounts and consecutive unusually high numbers
    if re.search(r'(([1-9]\d{2,},)+\d{3})|(\d{4,})', message):
        return True

    # If none of the above conditions are met, the message is likely not spam
    return False
