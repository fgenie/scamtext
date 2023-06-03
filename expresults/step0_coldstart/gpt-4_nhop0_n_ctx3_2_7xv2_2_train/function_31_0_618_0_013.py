
import re

def is_spam(text):
    # Common spam phrases and patterns
    spam_phrases = [
        "상한가",
        "익 절 가",
        "무료추천주",
        "수익률",
        "긴급입수정보",
        "투자반",
        "최소 금요일",
        "입장",
        "누적수익률",
        "FDA승인 임상3상완료",
        "종목/편입가",
        "최소 금요일",
        "1차목표가",
        "2차목표가",
        "3차목표가",
    ]

    # Check for spam phrases and patterns in the text
    for phrase in spam_phrases:
        if re.search(re.escape(phrase), text):
            return True

    # Check for short URLs, a common spam message feature
    short_links = re.findall(r'https?://me2\.kr/\w+', text)
    advanced_links = re.findall(r'https?://opcn-kakao\.com/\w+', text)

    if short_links or advanced_links:
        return True

    # If none of the spam features were found, the text is considered normal
    return False
