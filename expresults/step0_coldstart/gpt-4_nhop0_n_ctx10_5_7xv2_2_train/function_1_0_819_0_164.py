def is_spam(text):
    import re

    # Check for common spam words and phrases
    spam_words = ["신규정보", "목표가", "거래량", "야심한 기업", "수익률", "목돈", "빨간불급등", "10배", "25,000원", "믿고 넣어보세요", "공시발표", "국회의원", "비공개 상승주"]
    for word in spam_words:
        if word in text:
            return True

    # Check for suspicious URLs and phone numbers
    url_pattern = r'(https?://[^\s]+|bit\.ly/[^\s]+|me2\.kr/[^\s]+|kakaotalk\.it/[^\s]+|openkakao\.at/[^\s]+|dokdo\.in/[^\s]+)'
    phone_pattern = r"(\+\d{1,2}\s*)?\(*\d{2,4}\)*\s*(\d{1}[-\s]*\d{3,4}[-\s]*\d{4,5}|\d{4,5}[-\s]*\d{4,5})"
    url_match = re.search(url_pattern, text)
    phone_match = re.search(phone_pattern, text)
    if url_match or phone_match:
        return True

    # Check for repetitive characters (usually present in spam messages)
    repeat_pattern = r"([!@#$%^&*()_+\-=\[\]{}\\|;:'\",.<>/?`~]){2,}"
    repeat_match = re.search(repeat_pattern, text)
    if repeat_match:
        return True

    return False