
import re

def is_spam(message):
    # Define regular expressions for patterns typically found in spam messages
    url_regex = r"(http(s)?://|www\.)\S+"
    unusual_character_regex = r"[^a-zA-Z0-9\s,.?!]+"

    # Check if the message contains an URL
    if re.search(url_regex, message):
        
        # Check if the message contains unusual characters or not
        if re.search(unusual_character_regex, message):
            return True
    
    # Check if message contains a lot of numbers and percentages
    num_percent_pattern = r"[\d]+%\s?[\+]?↑?"
    if len(re.findall(num_percent_pattern, message)) > 2:
        return True

    # If none of the above conditions are satisfied, the message is considered normal
    return False
