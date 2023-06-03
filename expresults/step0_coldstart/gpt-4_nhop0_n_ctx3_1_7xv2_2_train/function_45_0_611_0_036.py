def is_spam(message):
    import re

    # Check if the message has a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Check if the message has special characters or numbers repeated multiple times
    repeat_pattern = re.compile(r'(\d{3,}|\W{3,})')
    has_repeats = bool(repeat_pattern.search(message))

    # Check if the message has words related to spam
    spam_words = ["송금", "종목", "투어", "투자", "당신이 승자", "회탄", "공짜",
                  "보내기", "하세요", "귀하", "클릭", "선물", "입장", "환불", "유료", "사기",
                  "나노", "입력", "인증", "등록", "지금", "가입", "추가", "정보",
                  "특가", "매출", "광고", "마감", "기회", "혜택", "참가", "우승", "혁신"]
    has_spam_words = any(spam_word in message for spam_word in spam_words)

    # If the message has a URL and at least one of the features (repeats, spam words), classify it as spam
    if has_url and (has_repeats or has_spam_words):
        return True
    else:
        return False