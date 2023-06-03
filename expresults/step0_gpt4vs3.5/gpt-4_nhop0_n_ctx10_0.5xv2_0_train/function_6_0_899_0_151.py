
import re

def is_spam(message):
    # Patterns
    url_pattern = r'http\S+'
    bonus_pattern = r'\d+(%)\s*(↑|↓)'
    money_pattern = r'\d+(원|만|천|백|십)?\s*(원|만|천|백|십)?'
    numberWithComma_pattern = r'\d{1,3}(,\d{3})*(\.\d+)?'
    emoji_pattern = r'[\U0001F600-\U0001F64F]'

    # Check patterns
    has_url = re.search(url_pattern, message)
    has_bonus = re.search(bonus_pattern, message)
    has_money = re.search(money_pattern, message)
    has_numberWithComma = re.search(numberWithComma_pattern, message)
    has_emoji = re.search(emoji_pattern, message)

    # If any of the patterns are found, return True (spam)
    if has_url or has_bonus or has_money or has_numberWithComma or has_emoji:
        return True
    
    # Otherwise, return False (not spam)
    return False
