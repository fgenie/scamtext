
import re

def is_spam(message):
    # Check if the message contains url
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    url_match = url_pattern.search(message)
    
    # Check for unusual characters in the message
    unusual_characters = re.findall(r"[^\w\s,\.\-?\!]+", message)
    
    # Check for excessive use of capital letters
    capital_letter_count = sum(1 for c in message if c.isupper())
    total_letter_count = sum(1 for c in message if c.isalpha())
    capital_ratio = capital_letter_count / total_letter_count if total_letter_count > 0 else 0
    
    # Check for common spam keywords
    spam_keywords = ['VIP', '추천', '클릭', '투자반', '루징', '공시발표']
    keyword_count = sum(1 for keyword in spam_keywords if keyword in message)
    
    # Set thresholds for spam classification
    url_threshold = 1
    unusual_char_threshold = 2
    capital_letter_threshold = 0.7
    keyword_threshold = 2
    
    # Classify the message as spam if any of the thresholds are passed
    if (url_match and url_threshold) or (len(unusual_characters) >= unusual_char_threshold) or (capital_ratio >= capital_letter_threshold) or (keyword_count >= keyword_threshold):
        return True
    return False
