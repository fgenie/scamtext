def is_spam(message: str) -> bool:
    import re

    # Check for typical spam words/phrases
    spam_keywords = [
        '축하합니다',
        '만원',
        '체험반',
        '비공개정보방',
        '감사',
        '수익',
        '상한가',
        '추천주',
        '월요일부터',
        '오후부터',
        '__기회__',
        '야너도',
        '클릭',
        '이벤트',
        '광고',
        '업데이트',
        '운영중',
    ]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for urls with suspicious domain names
    regex_url = r'https?://\S+'
    urls = re.findall(regex_url, message)
    
    spam_domains = [
        'me2.kr',
        'ko.gl',
        'kakaosa.co.kr',
        'han.gl',
        'bit.ly',
        'opcn-kakao.com',
        'vvd.bz',
        'vvvkauy.com',
        'dokdo.in'
    ]
    
    for url in urls:
        for domain in spam_domains:
            if domain in url:
                return True
    
    # Check for phone numbers, email addresses
    regex_phone_number = r'\d{2,4}-\d{3,4}-\d{3,4}'
    regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_numbers = re.findall(regex_phone_number, message)
    email_addresses = re.findall(regex_email, message)

    if phone_numbers or email_addresses:
        return True

    return False