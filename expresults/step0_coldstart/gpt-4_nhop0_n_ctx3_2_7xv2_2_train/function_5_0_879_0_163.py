def is_spam(message):
    import re

    # Check for suspicious keywords
    spam_keywords = ['마지막반', '체험', '적중', '시료', '소니드', '런던카지노', '신규', '감사', '출금', '카지노', '이벤트']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URL shorteners
    url_shorteners = ['me2.kr']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for excessive punctuation
    excessive_punctuation = re.compile(r'[\!-\?]{3,}')
    match = excessive_punctuation.search(message)
    if match:
        return True

    # Check for excessive emojis
    excessive_emojis = re.compile(r'[\u2600-\u26FF\u2700-\u27BF]{3,}')
    match = excessive_emojis.search(message)
    if match:
        return True

    # Check for excessive special symbols
    excessive_symbols = re.compile(r'★|▲|♥️|☞|🎈|👉|ⓒ|🌟|\<1️')
    match = excessive_symbols.search(message)
    if match:
        return True

    return False