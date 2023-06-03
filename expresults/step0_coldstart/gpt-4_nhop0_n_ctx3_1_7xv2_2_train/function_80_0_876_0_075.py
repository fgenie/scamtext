
import re

def is_spam(text):
    # Check for common spam phrases and patterns
    spam_phrases = ["광고", "지원", "투자", "선물", "계약", "최대", "지급", "교육", "이벤트", "소액", "수수료"]
    urls_pattern = r"(http(s)?://)?(www\.)?([a-z0-9\-]+\.)?[a-zA-Z0-9\-]+(\.[a-zA-Z]{2,5})+"
    codes_pattern = r"코드|입장코드"
    
    text = text.lower()
    
    # Check if any spam phrase is present in the text
    if any(spam_phrase in text for spam_phrase in spam_phrases):
        return True
        
    # Check if any URL pattern is present in the text
    if re.search(urls_pattern, text):
        return True
        
    # Check if any code pattern is present in the text
    if re.search(codes_pattern, text):
        return True
    
    return False
