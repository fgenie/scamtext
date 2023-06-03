
import re

def is_spam(message: str) -> bool:
    # Check for common spam phrases and patterns
    spam_patterns = [
        r'[\d\w]{5,10}\.com',  # Domain names with random characters
        r'\d+,(?:P|만원) 무료',  # Amount of currency as an incentive
        r'상한가',  # Stock trading
        r'https:\/\/(me2\.kr|bit\.ly)\/[\w\d]+',  # Shortened URLs
        r'후회안합니다',  # No regrets
        r'★\w+★',  # Surrounded by stars
        r'지금구매',  # Urgent buying call
        r'진행하겠습니다',  # Rushing the user
        r'발표', # Announcement
    ]

    # Check if any pattern is found in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
