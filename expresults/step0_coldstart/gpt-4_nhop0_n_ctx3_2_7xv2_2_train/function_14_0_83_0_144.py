def is_spam(message: str) -> bool:
    import re
    
    # Check for web발신
    if '[web발신]' in message:
        return True

    # Check for suspicious URLs
    if re.search(r'(http|https)://[^\s]*', message):
        if "tuney.kr" in message or "me2.kr" in message:
            return True

    # Check for 목표달성기념 or 상한가 확정
    if '목표달성기념' in message or '상한가 확정' in message:
        return True

    # Check for 트렌드 따라 or 긴급입수정보
    if '트렌드 따라' in message or '긴급입수정보' in message:
        return True

    # Check for excessive special characters
    if re.search(r"([!#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~])+", message):
        if len(re.findall(r"([!#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~])", message)) >= 4:
            return True
    
    return False