
import re


def is_spam(message: str) -> bool:
    # Check for presence of common spam words and phrases
    spam_keywords = [
        "광고", "입장코드", "1:1멘토링", "적중", 
        "수익금", "나스닥", "선물개미투자",
        "지원방", "지긋지긋한", "동학개미", "소액투자",
    ]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for presence of URL in message
    url_pattern = r'(https?://[^\s]+)'
    if re.search(url_pattern, message):
        return True

    # Check for presence of number sequences (e.g., prices, phone numbers)
    number_sequences = [r'\d{3,}', r'\d{1,3},\d{3}']
    for pattern in number_sequences:
        if re.search(pattern, message):
            return True

    return False
