def is_spam(message: str) -> bool:
    import re

    # Check for spam keywords
    spam_keywords = ['광고', '무료', '주식', '톡', '승인', '친구추가', '현대코퍼레이션', 'KEY', 'abit.ly', 'dokdo.in']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for shortened URL patterns
    url_patterns = [r"bit\.ly\/\w+", r"dokdo\.in\/\w+", r"open\.kakao\.com/o/[\w-]"]
    for pattern in url_patterns:
        if re.search(pattern, message):
            return True

    # Check for numerical sequences
    num_sequences = [r"\d+%\+매주", r"\d+만원", r"\d+분", r"\d+:\d+멘토링", r"\d+타임"]
    for seq in num_sequences:
        if re.search(seq, message):
            return True

    # If none of above patterns are found, consider the message as normal
    return False