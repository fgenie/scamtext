
import re

def is_spam(message: str) -> bool:
    # Set thresholds for spam identiﬁcation
    MAX_LINK_COUNT = 1
    MIN_SPAM_KEYWORD_COUNT = 2
    spam_keywords = ['광고', '입장', '수익률', '투자']

    # Search for links in the given message
    link_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    links = link_pattern.findall(message)

    # Check if the number of links is over the threshold
    if len(links) > MAX_LINK_COUNT:
        return True

    # Check for spam keywords in the message
    spam_keyword_count = sum([1 for keyword in spam_keywords if keyword in message])

    return spam_keyword_count >= MIN_SPAM_KEYWORD_COUNT
