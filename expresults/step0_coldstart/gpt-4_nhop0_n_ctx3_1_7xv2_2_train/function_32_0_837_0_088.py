
import re

def is_spam(message: str) -> bool:
    message = message.lower()

    # Spam trigger words and phrases
    spam_trigger_words = ["추천주", "투자반", "실력으로 입증", "자동으로", "마감"]

    # Check for spam trigger words
    for trigger in spam_trigger_words:
        if trigger in message:
            return True

    # Check for short URLs
    short_url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    short_urls = short_url_regex.findall(message)
    if len(short_urls) > 0:
        return True

    # Check for excessive numbers
    number_regex = re.compile(r'\d+')
    numbers = number_regex.findall(message)
    if len(numbers) > 2:
        return True

    return False
