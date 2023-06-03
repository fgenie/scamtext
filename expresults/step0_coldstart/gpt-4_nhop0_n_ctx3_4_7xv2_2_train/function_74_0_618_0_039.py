
import re

def is_spam(text):
    # Define spam keywords and patterns
    spam_keywords = ['무료입장', '트레이딩'] 
    spam_patterns = [
        r'https?:\/\/[\w\.-]+\/[\w\.-]+', 
        r'\d{2,4}년[^a-zA-Z0-9]{1,3}\d{1,4}%달성'
    ]
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True
            
    # If no spam keywords or patterns are found, return False
    return False
