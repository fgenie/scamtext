def is_spam(message: str) -> bool:
    import re

    # List of common spam words and phrases
    spam_words = [
        "축하",
        "상한가",
        "확정",
        "치료제",
        "공개",
        "다음타자",
        "C제약",
        "긴급입수정보",
        "관련주",
        "프로젝트",
        "참여",
        "입장",
        "상담",
        "문의",
        "빠르게",
        "지급",
        "체험반",
        "독보적인",
        "수익 실탁",
        "한농화성",
        "무료",
        "체험",
        "비밀번호",
        "VIP",
        "전환"
    ]

    # Check for url
    url_check = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)

    # Check for spam words
    spam_word_check = any(word in message for word in spam_words)

    if spam_word_check or url_check:
        return True
    else:
        return False