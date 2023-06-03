
import re

# Define the function is_spam
def is_spam(message):
    # Define a list of common spam words and phrases
    spam_words = ["축하드립니다", "공개합니다", "딴판", "실시합니다", "▲", "▼", "참여"]

    # Define spam URL pattern
    spam_url_pattern = re.compile(r'http(s)?://[^\s]*[단]?독립[방]?\.com')

    # Check for spam words in the given message
    for word in spam_words:
        if word in message:
            return True

    # Check for spam URL pattern in the given message
    if spam_url_pattern.search(message):
        return True

    # If none of the spam indicators are present, classify the message as normal
    return False
