
import re

def is_spam(message):
    # Check for terms commonly found in spam messages
    spam_terms = ['광고', '체험반', '축하합니다', '비용', '성과', '무료거부', '송장번호', '보내는분', '상품명', '위탁장소', '배송일자']
    
    if any(term in message for term in spam_terms):
        return True

    # Check for URL shortening patterns
    regex = re.compile(r'(?:https?://)?(?:www\.)?\S*\.(?:me|kr|gg|bit)\S*')
    matches = re.findall(regex, message)
    
    if len(matches) > 0:
        return True

    # Check if message contains phone numbers with more than 7 digits
    phone_regex = re.compile(r'\d{7}\d*')
    phone_matches = re.findall(phone_regex, message)

    if len(phone_matches) > 0:
        return True
    
    return False
