
import re

def is_spam(message):
    # Check for the presence of multiple links
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(links) > 1:
        return True

    # Check for the presence of shortened links or fake domains
    suspicious_link = re.search(r'(opcn-kakao\.com)|(openkakao\.io)', message)
    if suspicious_link:
        return True

    # Check for the presence of multiple '%' and numbers
    percentages = re.findall(r'\d+%+|%+\d+', message)
    if len(percentages) > 1:
        return True

    # Check for the presence of multiple numbers followed by the word '원'
    currency_numbers = re.findall(r'\d.*,.*원+', message)
    if len(currency_numbers) > 1:
        return True

    # Check for phrases commonly associated with spam messages
    spam_phrases = ['대한민국 no.1', '온라인 GAME', 'VIP 담당 에이전시', '약속 드립니다',
                    '정보방에서 상세히 바로 공개됩니다', '전문가 경력', '누적수익률']
    for phrase in spam_phrases:
        if phrase in message:
            return True
    return False
