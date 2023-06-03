def is_spam(message: str) -> bool:
    import re

    # Conditions for detecting spam messages
    # 1. Contains URL
    url_pattern = re.compile(r'https?:\/\/[\S]+')
    if url_pattern.search(message):
        return True

    # 2. Contains unusual characters or excessive punctuation
    unusual_character_pattern = re.compile(r'[\W\d]{3,}')
    if unusual_character_pattern.search(message):
        return True

    # 3. Contains suspicious keywords
    suspicious_keywords = [
        r'추천주', r'상한가', r'적중', r'혜택', r'주식',
        r'화성 30%↑', r'인수합병', r'만에', r'입장 안내',
        r'명가로와주세요', r'국자 자동 투자', r'오픈합니다', r'대박',
        r'정회원방', r'월 체험반', r'전량 척결'
    ]
    
    for keyword in suspicious_keywords:
        if re.search(keyword, message):
            return True
    
    # If none of the conditions are met, the message is not spam
    return False