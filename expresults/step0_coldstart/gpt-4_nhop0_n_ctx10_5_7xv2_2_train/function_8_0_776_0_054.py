
import re

def is_spam(text):
    # Check for common spam keywords
    spam_keywords = [
        "광고", "상한가", "추천종목", "수익률", "익절가",
        "목표가", "발표시", "예상상승", "무료문자", "무료거부",
        "결제", "기회", "특가", "선착순", "비밀번호",
        "체험", "최고가성비", "이벤트"
    ]

    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    if url_pattern.findall(text):
        return True
  
    # Check if the text has a higher proportion of digits
    digits_regex = re.compile(r'\d')
    digits_count = len(digits_regex.findall(text))

    if digits_count / len(text) > 0.2:
        return True

    return False
