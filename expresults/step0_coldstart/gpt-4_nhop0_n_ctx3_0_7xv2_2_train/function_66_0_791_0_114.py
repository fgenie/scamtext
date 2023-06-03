def is_spam(message):
    import re

    # Check for spam keywords
    spam_keywords = ['추천', 'vip', '체험반', '분석', '현금', '정보', '초대', '코드', '광고', '성공', '수익률', '상한가', '무료체험', '종목', '상승', '기회', '월요일', '투자', '결과']

    for keyword in spam_keywords:
        if keyword in message.lower():
            return True

    # Check for URLs with non-standard domains
    urls = re.findall('https?:\/\/(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    spam_domains = ['me2.kr']
    
    for url in urls:
        for domain in spam_domains:
            if domain in url:
                return True

    # Check for phone numbers with specific formats
    phone_numbers = re.findall('\d{4}[-.\s]?\d{4}', message) # XXXX-XXXX
    if phone_numbers:
        return True

    # Check for excessive use of special characters
    if len(re.findall('[!?\*%$#]', message)) > 3:
        return True

    # If none of the above conditions are met, it's likely a normal message
    return False