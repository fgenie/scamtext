def is_spam(message: str) -> bool:
    import re

    # Check for common spam words and phrases
    spam_words = ['슈퍼개미', '대표', '수익', '부자', '노하우', '공개', '오픈채팅방', '종목',
                  '케이공간', '무료 공부교실', '구독', '공시발표', '단독입수', '수익달성', '%',
                  '체험반', '셀트리온헬스케어', '데일리베스트']

    # Check for URL patterns
    urls_pattern = re.compile(r'https?://\S+')

    # Calculate spam points
    spam_points = 0

    # Check for spam words in the message
    for word in spam_words:
        if word in message:
            spam_points += 1

    # Check for URLs in the message
    if urls_pattern.search(message):
        spam_points += 1

    # A message is considered spam if it has more than two spam points
    return spam_points > 2