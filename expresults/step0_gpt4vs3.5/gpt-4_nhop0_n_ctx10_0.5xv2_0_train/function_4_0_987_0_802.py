def is_spam(message):
    import re
    
    # Check for short URLs
    short_urls = re.compile(r'(?:https?:\/\/)?(?:bit\.ly|me2\.(kr|do)|ko\.gl).+')
    if short_urls.search(message):
        return True
        
    # Check for uncommon characters & words
    uncommon_chars = re.compile(r'[^\uAC00-\uD7A3]')
    odd_words = ["자동으로 편리하게", "VIP비공개정보방", "만원 준비"]
    
    if uncommon_chars.search(message) or any(w in message for w in odd_words):
        return True
    
    # Check for suspicious financial expressions
    financial_terms = re.compile(r'\d{1,3}[,\.]\d{3,}\s*[가-힣]*')
    if financial_terms.search(message):
        return True
    
    # Check for specific sentence patterns
    pattern = re.compile(r'\d{1,2}[월일|日]\s*[가-힣]*\s*[가-힣\s+]+\s*반\s*[가-힣]*\s*[가-힣0-9]+')
    if pattern.search(message):
        return True
    
    return False