import re

def is_spam(message: str) -> bool:
    # Check for shortlinks
    shortlink_pattern = re.compile(r'(bit\.ly|t\.co|goo\.gl|tinyurl\.com|ow\.ly|qgtq\.com|yotqt\.com|openkakao\.io)\S*')
    shortlink_result = shortlink_pattern.search(message)

    # Check for typical spam phrases
    spam_phrases = [
        '소니드',
        '적중',
        '다음주 종목도 오픈합니다',
        '지 원 금 혜택으로',
        '원으로',
        '신청 하신방',
        '입장 안내 드립니다',
        '↓ 클릭'
    ]

    # Lowercase the message
    message_lowercase = message.lower()

    # Check for any occurrence of spam phrases
    spam_phrases_result = any(phrase.lower() in message_lowercase for phrase in spam_phrases)

    # Determine if the message is spam
    spam = bool(shortlink_result) or spam_phrases_result

    return spam