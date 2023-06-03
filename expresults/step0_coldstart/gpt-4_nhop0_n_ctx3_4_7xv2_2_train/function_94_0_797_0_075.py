
import re

def is_spam(message: str) -> bool:
    # Check for common spam indicators
    spam_indicators = [
        r'\d+,?\d{3},?\d{3}',
        r'http[s]?://[^\s]+',
        r'익 \절 가',
        r'\d+%\S+\w',
        r'\d{4}년',
        r'안전거래소지원금지급',
        r'입장코드',
        r'\[ 클릭 종목확인 \]',
        r'(광고)',
        r'시작하세요',
        r'\d{1,2}월',
        r'수익률',
        r'(최대|최소)',
        r'월 최대'
    ]

    # Use regular expressions to check if any of the spam indicators are present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    # If none of the spam indicators are found, classify the message as not spam
    return False
