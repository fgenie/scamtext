
import re

def is_spam(message):
    message = message.lower()
    
    spam_indicators = [
        r'\d{1,2}%\s*[↑]',  # Text with percentage increase in spam example
        r'https?://\S+',  # URL in the message
        r'(상한가|탈모치료제|귀하의|계좌에)',  # Keywords related to spam
        r'(\(광고\)|\[신한은행\])',  # Advertisement indicators
    ]
    
    normal_indicators = [
        r'(안녕하세요|감사합니다|잘 지내시죠|하이|네)',
        r'연락( 드리겠습니다| 주셔서 감사합니다)',
    ]
    
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    
    for indicator in normal_indicators:
        if re.search(indicator, message):
            return False

    return False
