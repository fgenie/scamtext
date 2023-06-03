def is_spam(message: str) -> bool:
    import re

    # Check for common spam keywords
    spam_keywords = ["무료", "체험", "보증", "어 이벤트", "클릭", "유료", "매매", "투자", "가입", "전환", "특별", "코드", "알려드리", "개인연락", "암호"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters (e.g. multiple exclamation marks, question marks)
    if len(re.findall(r'[!?.]{2,}', message)) > 1:
        return True

    # Check if the message contains a suspicious URL
    suspicious_url_patterns = ["bit\.ly", "me2\.kr", "openkakao\.at"]
    for pattern in suspicious_url_patterns:
        if re.search(pattern, message):
            return True

    # Check for a large amount of numbers in the message
    if len(re.findall(r'\d+', message)) > 4:
        return True

    return False