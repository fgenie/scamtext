
import re

def is_spam(text):
    # Set initial score to 0
    spam_score = 0
    
    # Regular expressions matches repeated URLs, matching one URL multiple times
    repeated_url = r'(http|https|openkakao|kakaotalk|fastkakao)\S+\s(\1\S+\s)+'
    
    # Regular expressions matches numbers with commas, representing money amounts
    money_amount = r'([\d,]+원+)|([0-9]{1,3}(,[0-9]{3})*(원))'
    
    # Regular expressions matches ad or 광고 (Korean for advertisement) in the text
    ad_keywords = r'(광고)|(\(광고\))|(\[광고\])|([Aa][Dd])'
    
    # Regular expressions for finding phone numbers
    phone_numbers = r'(\d{3}-\d{3}-\d{4})|(\d{2,3}[- ]{1}\d{3,4}[- ]{1}\d{2,4})'
    
    # Check for repeated URLs
    if re.search(repeated_url, text):
        spam_score += 1
        
    # Check for money amounts
    if re.search(money_amount, text):
        spam_score += 1
        
    # Check for advertisement keywords
    if re.search(ad_keywords, text):
        spam_score += 1
        
    # Check for phone numbers
    if re.search(phone_numbers, text):
        spam_score += 1
    
    # If the spam_score is greater than or equal to 2, consider the message spam
    if spam_score >= 2:
        return True
    
    # If not, the message is not spam
    else:
        return False
