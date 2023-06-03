
import re

def is_spam(message):
    # Checking for the presence of a URL in the message
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    contains_url = re.search(url_pattern, message)

    # Checking for the presence of non-standard chars in the messages
    non_std_chars = re.search(r"\W+", message)

    # Checking for presence of some suspicious words
    suspicious_words = re.search(r"[0-9]+(?:일|만원)+|^(?=.{1,4}$)(?=[^가-힣]*[가-힣])(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])", message)
    
    # If the message contains a URL or suspicious words or non-standard characters, classify it as spam
    if contains_url or suspicious_words or non_std_chars:
        return True
    else:
        return False
