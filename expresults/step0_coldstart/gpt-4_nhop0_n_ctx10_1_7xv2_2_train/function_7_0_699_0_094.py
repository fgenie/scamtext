def is_spam(message: str) -> bool:
    import re

    # Check for excessive special characters in the message
    special_chars = re.findall(r'[-!$%^&*()_+|~=`{}\[\]:";<>?,./]', message)
    if len(special_chars) > len(message) / 4:
        return True

    # Check for excessive use of numbers in the message
    numbers = re.findall(r'\d+', message)
    if len(numbers) > 3:
        return True

    # Check for unusual percentage of uppercase characters in the message
    uppercase_chars = sum(1 for c in message if c.isupper())
    if uppercase_chars > len(message) / 3:
        return True

    # Check for presence of typical spam keywords
    spam_keywords = ["맞추세요!", "평생", "지급", "행복", "현명한 선택", "체험반", "부자", "달성", "올빼미 이벤트", "월 최대",
                     "무료 모의투자", "자동 입출금", "종료", "수익", "안전거래소지원금지급", "투자", "소득", "방법", "수익건수",
                     "가입코드", "외환", "광고", "추천코드", "카카오톡 오픈채팅방"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for presence of suspicious URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1:
        return True

    # The message has passed all the checks and is not considered as spam
    return False