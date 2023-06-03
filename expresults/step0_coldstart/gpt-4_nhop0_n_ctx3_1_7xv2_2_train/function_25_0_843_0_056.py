
import re

def is_spam(message):
    # Define patterns often found in spam messages
    url_pattern = r'https?://\S+'
    encoded_url_pattern = r'(\w+(?:\.)\w{2,})\/\w+'
    bitly_pattern = r'bit.ly/(\w+)'
    special_characters_pattern = r'[*%"_]'

    # Check for presence of patterns in input message 
    if re.search(url_pattern, message) or re.search(encoded_url_pattern, message) or re.search(bitly_pattern, message):
        return True
    if re.search(special_characters_pattern, message):
        special_characters_count = sum([1 for _ in re.finditer(special_characters_pattern, message)])
        if special_characters_count > 2:
            return True
    return False
