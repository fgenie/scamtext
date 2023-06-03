def is_spam(message: str) -> bool:

    import re
    
    # List of common spammy words
    spam_words = [
        "광고", "랜선", "셀프무료점검", "무료거부", "무료패키지", "탈퇴", "증선", "추천", "지난",
        "성공적", "파랑", "특별", "할인", "행사", "회원", "혜택", "추가", "종목", "나가요",
        "확정", "입장", "체크", "사업", "목표", "참여"
        "숙박", "이벤트"
    ]

    # Regular expressions for URLs, email addresses and phone numbers
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.＆+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._+-]+\.[a-zA-Z]{2,}")
    phone_pattern = re.compile(r"\d{2,4}-\d{2,4}-\d{4}")

    # Check if there is a URL or email or phone number
    has_url = bool(url_pattern.search(message))
    has_email = bool(email_pattern.search(message))
    has_phone = bool(phone_pattern.search(message))

    # If there is a URL, email, or phone number, tentatively consider it spam
    if has_url or has_email or has_phone:
        possible_spam = True
    else:
        possible_spam = False

    # Count the number of spammy words
    spam_word_count = sum([message.count(word) for word in spam_words])

    # If there are multiple spammy words, consider it spam
    multiple_spam_words = spam_word_count > 2

    # The final decision is based on whether there are multiple spammy words or any URL, email, or phone numbers
    is_spam_result = multiple_spam_words or possible_spam

    return is_spam_result