
import re

def is_spam(message):
    # Define spam characteristics
    url_pattern = r'(https?://[^\s]+|bit\.ly/\S+|han\.gl/\S+|me2\.kr/[^\s]+)'
    money_pattern = r'([0-9]+,?[0-9]*원)'
    emoji_pattern = r'[\U0001F601-\U0001F64F\U0001F680-\U0001F6C5\U0001F30D-\U0001F567]'
    
    # Count url, money, and emojis in messages
    url_count = len(re.findall(url_pattern, message))
    money_count = len(re.findall(money_pattern, message))
    emoji_count = len(re.findall(emoji_pattern, message))
    
    # Condition for spam
    if url_count > 0 and (money_count > 0 or emoji_count > 0):
        return True
    return False
