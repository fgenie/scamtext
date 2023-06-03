
import re

def is_spam(message):
    # Check for presence of URLs or special characters
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_found = bool(url_pattern.search(message))
    special_characters = '[%s]' % re.escape(r'!#$%&\'()*+,-./:;<=>?@[\]^^_`{|}~')

    # Count uppercase and special characters
    upper_count = sum(1 for c in message if c.isupper())
    special_count = len(re.findall(special_characters, message))

    # Calculate the proportion of content that is uppercase, special characters, and URLs
    total_chars = len(message)
    upper_prop = upper_count / total_chars
    special_prop = special_count / total_chars
    url_prop = url_found / total_chars

    # Decision based on thresholds for each criterion
    if upper_prop > 0.3 or special_prop > 0.1 or url_prop > 0.003:
        return True
    else:
        return False
