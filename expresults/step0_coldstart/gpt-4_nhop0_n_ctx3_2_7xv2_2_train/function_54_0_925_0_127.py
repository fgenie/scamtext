
import re

def is_spam(message: str) -> bool:
    # Check if message has multiple lines
    if message.count("\n") > 1:
        return True
        
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True
                
    # Check for percentage gains or losses
    percentage_gains_losses_pattern = re.compile(r'[0-9]+%\s?(?:↑|↓)')
    percentage_gains_losses = re.findall(percentage_gains_losses_pattern, message)
    if len(percentage_gains_losses) > 0:
        return True
        
    # If none of the spam indicators are found, return False
    return False
