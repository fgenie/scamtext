def is_spam(text):
    spam_keywords = ["광고", "추천주", "공개", "주주", "무료체험", "상한가", "이윤", "마감", "VIP", "빠르게", "현황", "me2.kr", "클릭", "정보방", "지난주", "dokdo.in", "안녕하세요", "알려드립니다", "단타정보", "수익률", "운영", "수익", "openkakao.io", "무료거부", "사활", "https://"]

    content = text.lower()
    for keyword in spam_keywords:
        if keyword.lower() in content:
            return True
    
    return False