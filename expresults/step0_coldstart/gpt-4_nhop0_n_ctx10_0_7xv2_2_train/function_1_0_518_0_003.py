
import re


def is_spam(text: str) -> bool:
    spam_keywords = [
        "추천",
        "공개",
        "신청",
        "적중",
        "정보방",
        "회원님",
        "초대",
        "배우고",
        "초I고",
        "ㅂ.H",
        "LIVE",
        "광고",
        "적립금",
        "증권사",
        "등록",
        "미공개종목",
        "체험",
        "VIP",
    ]

    normal_keywords = [
        "좋은 일만",
        "통화중",
        "여보",
        "주식 리딩방",
        "스팸",
        "게임",
        "오랜만",
        "하이",
        "돌았니",
        "운동 정보",
        "무료",
        "사전등록",
    ]

    text = text.lower()

    spam_count = 0
    for keyword in spam_keywords:
        if keyword in text:
            spam_count += 1

    normal_count = 0
    for keyword in normal_keywords:
        if keyword in text:
            normal_count += 1

    nums_urls = len(re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text))
    nums_phone = len(re.findall("\d{4}[ -)]?\d{4}", text))

    if spam_count > normal_count and nums_urls >= 1 or nums_phone >= 1:
        return True
    else:
        return False
