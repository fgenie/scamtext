
import re

def is_spam(message):
    # Check for common spam phrases or patterns
    spam_phrases = ["적중", "최고급 정보", "비용없습니다", "상승 확정", "현재 시장", "절대 강요", "오르기 전", "익절"]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
            
    # Check for multiple URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*[(]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    
    if len(urls) >= 2:
        return True
        
    # Check for percentage with more than two digits
    if re.search(r'\d{2,}%\s?[↑]?', message):
        return True

    # Check for short URLs
    if re.search(r'\b(?:https?:\/\/|me2\s*.\s*kr|\bvo\s*.\s*la)\S+', message, re.IGNORECASE):
        return True

    # Check for unusual patterns like repetition of the same short URL
    if re.search(r'(\b(?:https?:\/\/|openkakao\s*.+\s*at)\S+)\s+\1', message, re.IGNORECASE):
        return True

    return False
