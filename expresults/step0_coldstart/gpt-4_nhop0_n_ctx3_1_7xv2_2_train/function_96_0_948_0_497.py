
import re

def is_spam(message):
    # Detect the presence of multiple exclamation marks, numbers, and special characters
    excessive_symbols = re.findall(r'(!{2,}|\d+%|[={}\[\]/"$%^*+_`@~<>?,\.&:;"()-])', message)

    # Check for URL shorteners
    url_shorteners = re.findall(r'(bit\.ly|me2\.kr|buly\.kr)', message)

    # Check for phrases typically found in spam messages
    spam_phrases = re.findall(r'(슈퍼개미|공시발표|노하우|주식 공부방|따라만 하세요)', message)

    # Combine all the features found
    features = excessive_symbols + url_shorteners + spam_phrases

    # If any feature is present in the message, classify it as spam
    if len(features) > 0:
        return True
    else:
        return False
