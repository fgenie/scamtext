def is_spam(message):
    spam_keywords = ["바나바나", "고수익", "Vip방", "공시발표", "신 청 하 신", "openkakao", "opcn-kakao", "me2.kr"]
    normal_keywords = ["선생님", "부동산", "평택", "탈주", "제네시스", "연봉", "여기서", "여보", "주식", "리딩방"]

    spam_score = 0
    normal_score = 0

    for word in spam_keywords:
        if word in message:
            spam_score += 1

    for word in normal_keywords:
        if word in message:
            normal_score += 1

    return spam_score > normal_score