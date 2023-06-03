def is_spam(message):
    from re import search

    keywords = [
        "실력입증", "추천주", "잠시 시간내서", "지원금받기", "무료교육", "주식상담",
        "광고)", "추.천", "해외선물", "무료거부", "정회원방", "kakaotalk.it", "me2.kr",
        "선입수", "프로모션", "초대합니다", "특별케어", "완성", "체험반", "차별", "체험", "너도나도",
        "로또", "지식교환", "신세계 상품권", "치킨", "커피"
    ]

    def contains_keyword(text):
        for word in keywords:
            if word in text:
                return True
        return False

    def contains_url(text):
        return bool(search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))

    if contains_keyword(message) and contains_url(message):
        return True
    else:
        return False