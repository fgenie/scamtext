def is_spam(message: str) -> bool:
    import re

    # Check for suspicious keywords
    spam_keywords = ['[가-힣a-zA-Z0-9]{3,} vip', '폭등', '아줌마', '공시공개', '오픈초대', '해선', '단체방', '실력입증',
                     '추천주', '[가-힣a-zA-Z0-9]{3,} [0-9]{1,2}%↑', '다음주도', '체험반', '다음 타자']
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    # Check for suspicious URLs
    url_pattern = 'https?:\/\/(?:[\w]+\.)?[\w]+(?:\.[\w]+)+\/?[\w\#\-\.\?=\&%]*(?!\.\.)'
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        # Check for suspicious URL patterns
        suspicious_url_pattern = ['me2\.kr', '\.opu']
        for url in urls:
            for pattern in suspicious_url_pattern:
                if re.search(pattern, url):
                    return True

    return False