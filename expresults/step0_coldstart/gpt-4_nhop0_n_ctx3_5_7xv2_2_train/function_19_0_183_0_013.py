def is_spam(message):
    import re

    suspicious_terms = [
        '마감임박',
        '정회원',
        '투자반',
        '광고',
        '극복하세요',
        '수익',
        '익절',
        '무료혜택',
        '입장',
        '카톡방',
        '프로젝트',
        '컨설팅'
    ]

    threshold = 0.20
    count_suspicious_terms = sum([1 for term in suspicious_terms if term in message])
    spam_ratio = count_suspicious_terms / len(message)

    if spam_ratio > threshold:
        return True

    url_pattern = re.compile(r'(https?|ftp)://[^\s/$.?#].[^\s]*')
    if url_pattern.search(message) and count_suspicious_terms > 0:
        return True

    return False