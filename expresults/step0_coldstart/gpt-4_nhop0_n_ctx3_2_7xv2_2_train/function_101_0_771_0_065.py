
import re

def is_spam(message):
    # Regular expressions for common spam characteristics
    url_pattern = r'https?://\S+'
    price_pattern = r'\d[\d,]*원'
    code_pattern = r'코드\s*:\s*\d+'
    free_ad_rejection_pattern = r'무료거부'
    plus_sign_pattern = r'\+'
    special_ads_keyword = r'(광고)'
    
    # Use regular expressions to search for spam characteristics
    url_match = re.search(url_pattern, message)
    price_match = re.search(price_pattern, message)
    code_match = re.search(code_pattern, message)
    free_ad_rejection_match = re.search(free_ad_rejection_pattern, message)
    plus_sign_match = re.search(plus_sign_pattern, message)
    special_ads_match = re.search(special_ads_keyword, message)
    
    # Check if the message has spam characteristics
    if url_match or price_match or code_match or free_ad_rejection_match or plus_sign_match or special_ads_match:
        return True
    else:
        return False
