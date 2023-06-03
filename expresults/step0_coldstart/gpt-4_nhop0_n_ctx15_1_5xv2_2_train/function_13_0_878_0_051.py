def is_spam(message: str) -> bool:
    import re

    # Check for suspicious keywords
    spam_keywords = ["신규", "입금", "출금", "증권", "추천주",
                     "혜택", "악성광고", "무료추천", "전달",
                     "종목", "상승", "최소", "특허"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for links in message
    link_pattern = re.compile(r'(http|https:\/\/|www\.|bit\.ly|me2\.kr|kakao[^ ]*|talk[^ ]*|naver\.me|ko\.gl)[^ ]+')
    if re.search(link_pattern, message):
        return True

    # Check for percentages
    percent_pattern = re.compile(r'\d{1,3}%')
    if re.search(percent_pattern, message):
        return True

    return False