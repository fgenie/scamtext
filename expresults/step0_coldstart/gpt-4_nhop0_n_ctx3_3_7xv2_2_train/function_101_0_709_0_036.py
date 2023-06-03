def is_spam(message):
    import re

    spam_keywords = [
        "추천주", "현황", "체험반", "정확한 분석", "검증된 수익률", "종목상담",
        "상장기업", "수요일", "화제", "https", "me2.kr", "bit.ly"
    ]

    normal_keywords = [
        "머하냐", "밥먹자", "롤", "주식함", "주식 있음", "야 술먹자", "오키"
    ]


    # Calculate spam keyword count
    spam_count = 0
    for keyword in spam_keywords:
        spam_count += len(re.findall(re.escape(keyword), message))

    # Calculate normal keyword count
    normal_count = 0
    for keyword in normal_keywords:
        normal_count += len(re.findall(re.escape(keyword), message))

    # Check if spam or not
    return spam_count > normal_count