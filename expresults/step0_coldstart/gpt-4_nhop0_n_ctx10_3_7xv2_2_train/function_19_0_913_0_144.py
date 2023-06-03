
import re

def is_spam(message):
    # Check for common spam indicators
    spam_indicators = [
        r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',  # URLs
        r'\d+%?',  # Percentage
        r'\d+\d*[,\.]?\d{3}',  # Large numbers
        r'\b(광고|혜자|공짜|특가|할인|상한가|상승|무료거부|무료|이벤트|지원|수익률|최소|최대|AI|로봇사업|특허|모험)\b',  # Spam keywords
        r'\b(입력코드|입장코드|코드|바로 증정|바로증정|에어드로프|공짜로 받으세요|공짜 받으세요|공짜받으세요)\b',  # Spam phrases
    ]

    # Check if any spam indicators are present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    # If no spam indicators are found, classify the message as non-spam
    return False
