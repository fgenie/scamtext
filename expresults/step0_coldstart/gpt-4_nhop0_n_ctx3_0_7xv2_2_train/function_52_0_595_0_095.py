
import re

def is_spam(text: str) -> bool:
    # Check for spam characteristics such as repeated phrases, and suspicious URLs
    text = text.lower()
    repeated_phrases = re.findall(r'(\b\w+\b)(?=.*\1)', text)
    suspicious_urls = re.findall(r'(openkakao\.it\/\w+)|(me2\.kr\/\w+)', text)

    # Check for presence of advertising phrases
    advertising_phrases = ['상한가', '최소 150% 이상 상승', '익절', '손실 없습니다',
                           '무료 이며', '목표가', '정치세력']

    for phrase in advertising_phrases:
        if phrase in text:
            return True

    # Check for positive/negative words/phrases that would be found in normal messages
    normal_phrases = ['잘 지내지?', '안녕하세요', '만 나오기 전', '테마주', '수급주']

    for phrase in normal_phrases:
        if phrase in text:
            return False

    # If message contains repeated phrases, suspicious URLs, or has a high percentage of capitalized content, classify as spam
    capital_ratio = sum(1 for c in text if c.isupper()) / len(text)
    if repeated_phrases or suspicious_urls or capital_ratio > 0.3:
        return True

    return False
