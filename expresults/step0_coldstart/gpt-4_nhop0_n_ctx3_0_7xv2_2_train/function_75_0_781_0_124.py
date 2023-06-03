def is_spam(message):
    import re

    # Patterns to detect spam messages
    spam_patterns = [
        r"(긴급히|빠른 확인|연락)",
        r"(증권|공시|종목)",
        r"(\d{2,3}%|상승)",
        r"((당신은|더이상 정보가 아닙니다|내일 추천드릴 종목|오전 9시에 종목 오픈하겠습니다|교환)까지)",
        r"(openkakao.it)",
        r"(https?://[^\s]+)",
        r"(대규모투자)",        
    ]

    # Join patterns and compile as regex
    spam_regex = re.compile("|".join(spam_patterns), re.IGNORECASE)

    # Check for presence of spam keywords or patterns
    if spam_regex.search(message):
        return True
    else:
        return False