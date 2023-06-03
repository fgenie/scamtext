def is_spam(message: str) -> bool:

    import re
    
    keywords = [
        "추천주", "단독발표정보", "체험VIP", "상한가확정",
        "증권사부장", "코 인", "수익률", "모의투자대회",
        "주식", "마감방식", "매일", "버는방법",
        "주최소", "종목", "안정적인"
    ]

    message = message.lower()

    # Check for too many consecutive special characters
    special_char_re = re.compile(r'[~`!@#$%\^&*\(\)_+\-=\[\]{}\\|;\'\",.<>/?]+')
    consecutive_chars = special_char_re.findall(message)
    for chars in consecutive_chars:
        if len(chars) > 3:
            return True

    is_spam = False

    for keyword in keywords:
        if keyword.lower() in message:
            is_spam = True
            break

    return is_spam
