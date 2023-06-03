
import re

def is_spam(text: str) -> bool:
    # Check for common spam indicators
    spam_indicators = [
        r'\b광고\b',
        r'(?:http|https)://\S+',
        r'\b80% 상승\b',
        r'\b정부정책과 대주주의 성향을 읽고\b',
        r'\b무료거부\b',
        r'\b텔레그램으로 이동합니다\b',
        r'\d+% 금일 증권사 매집주 공개하겠습니다'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True

    return False
