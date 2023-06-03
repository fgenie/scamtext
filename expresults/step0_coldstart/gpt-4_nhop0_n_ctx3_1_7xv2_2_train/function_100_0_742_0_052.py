import re

def is_spam(text):
    # Check for URL patterns with shorteners or suspicious links
    url_pattern = re.compile(r'(http(s)?://)?(me2\.|ok4\.at|bit\.ly|goo\.gl|tinyurl\.com)')
    if url_pattern.search(text):
        return True
    
    # Checking if the message content contains keywords commonly used in spam messages
    spam_keywords = ['🔺', 'VIP', '비공개', '수익률', '참가', '체험반', '추천주', '수익내기 프로젝트', '외 준비된', '진입하시길', '익절하지마세요', '물량 매집']
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    # Check for message patterns indicating advertising or business promotions
    ad_pattern = re.compile(r'\(광고\)|\(선착순|무료|수수료|한정수량|특별이벤트|상담|전화번호|할인|혜택')
    if ad_pattern.search(text):
        return True

    # If none of the above conditions are met, consider the message normal
    return False