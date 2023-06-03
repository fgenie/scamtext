def is_spam(message):
    import re

    # Spam trigger words or phrases
    spam_keywords = ['목표달성기념', '추천 디젠스', '추천드릴 종목', '최소 150% 이상 상승', '익절입니다', '주식은 오를때']
    
    # Check for suspicious URL patterns
    urls = ['me2.kr', 'tuney.kr', 'openkakao.io']
    url_pattern = re.compile(r'(https?://\S+)')
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    urls_found = re.findall(url_pattern, message)
    
    for found_url in urls_found:
        for url in urls:
            if url in found_url:
                return True
    
    return False