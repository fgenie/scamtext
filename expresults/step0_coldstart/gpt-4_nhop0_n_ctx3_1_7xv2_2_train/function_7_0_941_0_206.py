
import re

def is_spam(message):
    # Check for multiple consecutive non-alphanumeric characters
    non_alphanumeric_count = len(re.findall(r'\W{2,}', message))
    if non_alphanumeric_count > 1:
        return True
        
    # Check for URL shorteners
    shorteners = ['bit.ly', 'me2.kr', 'kakaosa.co.kr', 'buly.kr']
    if any(shortener in message for shortener in shorteners):
        return True

    # Check for suspicious keywords related to spam
    spam_keywords = ['월요일부터', '주식', '수익', '추천주', 'VIP체험반', '증권사', '타점/분석', '광고', '실시간차트', '검색어']
    if any(keyword in message for keyword in spam_keywords):
        return True
        
    # Check for money amounts
    amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', message)
    if amounts and len(amounts) >= 2:
        return True

    return False
