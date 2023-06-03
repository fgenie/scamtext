def is_spam(text):
    import re
    from collections import Counter

    # Check if message is significantly shorter than average
    if len(text) < 30:
        return False

    # Check for url shorteners
    url_shorteners = ['bit.ly', 'me2.kr', 'han.gl', 'i.kiwoom.com', 'openkakao', 'kakaotalk', 'naver.me']
    for shortener in url_shorteners:
        if shortener in text:
            return True

    # Check for common spam phrases in multiple languages
    spam_phrases = ['현대 인수합병 최종논의단계', '최소6배', '공개', '최소 150%', '완화', '공시발표', '기술특허임박', '목표달성기념',
                    '이벤트 진행', '경품', '무료 체험']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for spam-like patterns (e.g., special characters, excessive capitalization and numbers)
    special_characters = re.compile(r'\W')
    uppercase_letters = re.compile(r'[A-Z]')
    numbers = re.compile(r'\d')

    char_ratio = Counter(text)
    num_special = len(re.findall(special_characters, text))
    num_upper = len(re.findall(uppercase_letters, text))
    num_numbers = len(re.findall(numbers, text))

    ratio_special = num_special / len(text)
    ratio_upper = num_upper / len(text)
    ratio_numbers = num_numbers / len(text)

    if ratio_special >= 0.2 or ratio_upper >= 0.5 or ratio_numbers >= 0.5:
        return True

    # If none of the conditions are met, classify the message as normal
    return False