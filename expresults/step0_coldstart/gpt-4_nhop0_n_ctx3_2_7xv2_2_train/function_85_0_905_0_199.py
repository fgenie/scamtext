
import re

def is_spam(message: str) -> bool:
    # Check for unusual patterns in the text such as too many special characters or numbers
    special_characters = re.findall(r'[^\w\s]', message)
    numbers = re.findall(r'\d+', message)
    consecutive_spaces = re.findall(r'\s{2,}', message)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(],:?;|[]])+', message)

    # If there are more than 2 special characters or numbers, consider it as spam
    if len(special_characters) > 2 or len(numbers) > 2:
        return True
    
    # If there are more than 1 consecutive spaces, consider it as spam
    if len(consecutive_spaces) > 1:
        return True
    
    # If there is a url in the message, consider it as spam
    if len(urls) > 0:
        return True
    
    return False
