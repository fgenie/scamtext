
import re

def is_spam(message):
    spaminess_score = 0
    
    # Calculate spaminess_score based on special characters and uncommon symbols
    strange_symbols = re.findall(r"[^a-zA-Z0-9\s\.,!?@]", message)
    spaminess_score += len(strange_symbols)

    # Calculate spaminess_score based on overuse of uppercase letters
    uppercase_ratio = sum(1 for c in message if c.isupper()) / len(message)
    if uppercase_ratio > 0.6:
        spaminess_score += 10

    # Calculate spaminess_score based on web links that don't use https
    non_https_links = re.findall(r"http://\S+", message)
    spaminess_score += len(non_https_links) * 5
    
    # If the spaminess_score is above a certain threshold, classify message as spam
    if spaminess_score > 20:
        return True
    else:
        return False
