
import re

def is_spam(message: str) -> bool:
    # Check for common keywords in spam messages
    spam_keywords = ["지원금", "출금가능", "예상", "투자", "클릭", "code", "광고", "event", "bit.ly"]
    
    # Check for uncommon characters or combination of characters in spam messages
    spam_chars = ["▼", "☆", "★", "◀", "■", "=","(광고)"]
    
    # Check for URL shorteners commonly found in spam messages
    spam_url_shorteners = ["bit.ly", "me2.kr"]

    # If the message contains any of the aforementioned spam keywords, characters or URL shorteners, consider it spam
    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            return True
    for char in spam_chars:
        if char in message:
            return True
    for url_shortener in spam_url_shorteners:
        if url_shortener in message:
            return True

    # If the message is not spam, consider it a normal message
    return False

