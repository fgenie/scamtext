def is_spam(message: str) -> bool:
    import re

    # Check for common spam phrases and patterns
    spam_phrases = ['당첨 되셨습니다', '공시발표', '급등예정', '증권사 매집주 공개', '정회원방 입장']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for excessive use of symbols
    symbols_pattern = r'[!@#\$%\^&\*\(\)\-_=+\[\]\{\};:"\|,.<>/?~`§※✭]'
    if len(re.findall(symbols_pattern, message)) > 5:
        return True

    # Check for suspicious urls
    url_pattern = r'(?:http|https)://|bit\.ly|han\.gl|me2\.kr|gg\.gg|buly\.kr|openkakao\.at|abit\.ly'
    if re.search(url_pattern, message):
        return True

    # Check for excessive use of numbers or any potential monetary values
    numbers_pattern = r'\d{4,}|[0-9]+원|[0-9]+,\d{3,}|[0-9]+%\s*\+'
    if re.search(numbers_pattern, message):
        return True

    return False