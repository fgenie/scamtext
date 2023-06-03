
import re

def is_spam(message: str) -> bool:
    
    # Check for the presence of URLs in the message
    url_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_regex, message)
    
    # Check for non-standard URLs
    non_standard_url = False
    for url in urls:
        if not url.startswith("http://") and not url.startswith("https://"):
            non_standard_url = True
            break
    
    # Check for the presence of keywords commonly associated with spam messages
    spam_keywords = ["제재", "악성광고", "차별화 된", "실력으로 입증"]
    contains_spam_keywords = any(keyword in message for keyword in spam_keywords)
    
    return non_standard_url or contains_spam_keywords

