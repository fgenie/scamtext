def is_spam(message):
    import re

    spam_keywords = [
        "광고", "일체 비용없", "무료거부", "추가이벤트", "최고급 정보", "특별 혜택",
        "몇 %이상 상승 확정", "증시에서 가장 자유로운 투자상품",
        "오픈방 커뮤니티", "증시가 무너지는 상황", "주식은 오를 때 사는게 아니라 오르기 전",
        "무료리딩", "상담 문의", "신규 가입", "무조건 올라갑니다", "상한가달성"
    ]

    normalized_message = re.sub(r'\W+', ' ', message.lower())

    for keyword in spam_keywords:
        if keyword in normalized_message:
            return True

    return False