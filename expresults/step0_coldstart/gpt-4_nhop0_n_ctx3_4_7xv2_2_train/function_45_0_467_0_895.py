def is_spam(message):
    import re

    # Compile common spam keywords and phrases
    spam_keywords = [
        r"광고", r"지원받", r"지푸라기",
        r"수익금", r"소액투자", r"잡고 싶던", r"무료거부",
        r"기회를 잡으십시오", r"즉시 지원", r"수익을 보장",
        r"입장코드", r"특별한 프로모션", r"빠르게 돈을 벌",
        r"매우 높은 수익", r"\d{1,3}%"
    ]

    # Compile some common normal message patterns
    normal_keywords = [
        r"[a-zA-Z]", r"병원", r"수업",
        r"학교", r"계획", r"회의", r"가족",
        r"주말", r"초대", r"도착", r"체험",
        r"출장", r"행사", r"비행", r"미팅"
    ]

    # Check if the message contains any spam keywords or phrases
    if any(re.search(spam_pattern, message) for spam_pattern in spam_keywords):
        return True

    # Check if the message contains any normal keywords or phrases
    if any(re.search(normal_pattern, message) for normal_pattern in normal_keywords):
        return False

    # Default to spam if no specific keywords or patterns are found
    return True