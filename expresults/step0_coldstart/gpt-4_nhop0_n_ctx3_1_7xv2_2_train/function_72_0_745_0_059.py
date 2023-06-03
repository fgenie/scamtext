def is_spam(message: str) -> bool:
    import re

    # Check for common spam indicators
    spam_indicators = [
        r'\(광고\)',
        r'\b비용요구\b',
        r'\d{2,3}[,.]\d{2,3}[,.]\d{2,3}',
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'무료거부',
        r'성과',
        r'상품 목록',
        r'최근 \d개월 성공현황',
        r'자본액 \d+',
        r'정확한 정보와 상호 소통을 통해',
        r'경제 불황으로 많이 어려운 시기',
        r'투자',
    ]
    
    # Check for any matches in the message text
    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True
            
    # If no matches found, consider message as not spam
    return False