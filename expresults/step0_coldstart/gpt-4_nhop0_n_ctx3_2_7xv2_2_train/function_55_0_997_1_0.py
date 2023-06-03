
import re

def is_spam(message):
    # Check for multiple consecutive characters (e.g. !!!, ??, +++):
    if re.search(r"([!?,+]){2,}", message):
        return True
    
    # Check for links with suspicious endings (e.g. .kr)
    if re.search(r"(https?:\/\/\S+\.(?:me2|kr)\S*)", message):
        return True
    
    # Check if the message length is too long:
    if len(message) >= 100:
        return True

    # Check for non-latin characters:
    if re.search(r"[^a-zA-Z\d(\s\.,?!)]", message):
        return True

    return False
