
import re

def is_spam(message):
    # Checking for common spammy elements like links, unicode characters, or excessive punctuation.
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message):
        return True

    if re.findall(r'[\u4e00-\u9fff]+', message):
        return True

    if re.findall(r'[!?.+\-:^_*]+', message) and len(re.findall(r'[!?.+\-:^_*]+', message)) > 3:
        return True

    # Check for spammy special symbols or recurring uppercase in the text
    if re.search(r'[☆★%$€\[\]]+', message) or (len(re.findall(r'[A-Z]', message)) / len(message)) > 0.5:
        return True

    # Check for number/code sequences or ██████ patterns, typically found in spam messages
    if re.search(r'\d{5,}', message) or re.search(r'[█]+', message):
        return True
    
    return False
