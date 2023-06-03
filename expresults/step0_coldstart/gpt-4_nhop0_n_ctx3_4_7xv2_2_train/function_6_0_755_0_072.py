
import re

def is_spam(message):
    # Check for spam keywords
    spam_keywords = ['목표달성기념', '추천', '종목']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for excessive use of symbols
    symbols = ['^', '*', '%', '@']
    
    symbol_count = sum([message.count(symbol) for symbol in symbols])
    if symbol_count > 2:
        return True
    
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # If none of the above conditions are met, the message is considered normal
    return False
