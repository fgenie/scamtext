
import re

def is_spam(message):
    # Check for the presence of a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = url_pattern.search(message) is not None
    
    # Check for numbers and special characters common in spam messages
    number_pattern = re.compile(r'\d')
    has_numbers = number_pattern.search(message) is not None
    has_special_char = any(char in message for char in "'!%^_;,[]")

    # Check if the message contains financial or investment-related terms
    has_fin_terms = any(term in message for term in ["원", "투자", "수익", "매매"])

    return has_url and (has_numbers or has_special_char) and has_fin_terms

