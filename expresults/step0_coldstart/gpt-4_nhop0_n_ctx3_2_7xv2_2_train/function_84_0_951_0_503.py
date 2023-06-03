def is_spam(message: str) -> bool:
    import re

    # Rule 1: Check for URLs with suspicious patterns (shortened or obfuscated)
    url_pattern = r'(https?:\/\/)?(bit\.ly|adf\.ly|goo\.gl|tinyurl|bitly|rlu|bc\.vc|ow\.ly)\/\S+'
    
    # Rule 2: Check for excessive use of special characters
    special_chars_pattern = r'[!@#$%^&*(),.?":{}|<>]+'

    # Rule 3: Check for random mix of upper and lower case letters, digits, and special characters
    random_mixed_pattern = r'(\w*[A-Z]+\w*[a-z]+\w*[_\W]+\w*|\w*[a-z]+\w*[A-Z]+\w*[_\W]+\w*|\w*[_\W]+\w*[A-Z]+\w*[a-z]+\w*|\w*[A-Z]+\w*[_\W]+\w*[a-z]+\w*|\w*[a-z]+\w*[_\W]+\w*[A-Z]+\w*|\w*[_\W]+\w*[a-z]+\w*[A-Z]+\w*)'

    # Rule 4: Check for spam keywords
    spam_keywords = ['당신의 신용 점수를 향상', '비밀 충전', '무료 처리', '무료 상담', '다운로드 무료', '돈을 좋아하는']

    # Apply rules to the message
    if re.search(url_pattern, message) or re.search(special_chars_pattern, message) or re.search(random_mixed_pattern, message):
        return True
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False