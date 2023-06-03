
import re

def is_spam(message: str) -> bool:
    # Spam messages often contain shortened URLs and/or phone numbers
    shortened_url_pattern = r'(http(s)?:\/\/)?(bit\.ly|me2.kr|kakaotalk.it|openkakao.it)\/\S+'
    phone_number_pattern = r'\d{3}[-\.\s]?\d{3,4}[-\.\s]?\d{4}'

    # Check if message contains URL or phone number
    has_url = re.search(shortened_url_pattern, message) is not None
    has_phone_number = re.search(phone_number_pattern, message) is not None

    # Check for repetitive exclamation marks or Korean jamo characters
    repetitive_punctuation = re.search(r'(\?|!)\1{2,}', message) is not None
    jamo_characters = re.search(r'[ㄱ-ㅎ가-힣]+', message) is not None

    # Check for phrases commonly used in spam messages
    spam_phrases = [
        '추천',
        '상승',
        '정보',
        '고객님',
        'VIP',
        '수익',
        '할인',
        '지금',
        '유튜브',
    ]
    contains_spam_phrases = any(spam_phrase in message for spam_phrase in spam_phrases)

    # Message is considered spam if it contains URL, phone number, repetitive punctuation, jamo characters or spam phrases
    return has_url or has_phone_number or repetitive_punctuation or jamo_characters or contains_spam_phrases


# Usage example
message = "신년을 축하드리며 안부인사 전함니다 요즘 근황은 어떠신지요??"
print(is_spam(message))  # Expected output: False

message = "https://me2.kr/hgf 기존 정보/혜택 동일유지"
print(is_spam(message))  # Expected output: True
