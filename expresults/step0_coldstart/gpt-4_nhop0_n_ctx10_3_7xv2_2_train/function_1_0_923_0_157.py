def is_spam(message: str) -> bool:
    import re

    # Check for typical spam keywords, phrases, and symbols
    spam_keywords = [
        "적중",
        "미공개종목",
        "공개",
        "무료",
        "광고",
        "약속",
        "보상",
        "수익",
        "매수",
        "결과",
        "상한가",
        "지켜만 보세요",
        "클릭",
        "무조건",
        "강요하지 않습니다",
        "안 사셔도 됩니다",
        "500%",
        "기업세력",
        "종목 정보",
        "차별화된 정보",
        "수익보시고나서 감사하다고 인사한번 주시는건 어렵지않으실겁니다",
        "무료거부",
        "체험반",
        "공시정보"]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for multiple links (shortened or not) in the message
    urls = re.findall(r'(https?://\S+)', message)
    if len(urls) > 1:
        return True

    # Check for money, percentage or number expressions which often appear in spam messages
    money_regex = r'(\d{1,3}(?:,\d{3,})*(?:\.\d{1,2})?|[1-9]\d{0,2}(?:\.\d{1,2})?%|\d{1,3}원|예상|수익|퍼센트)'
    if re.search(money_regex, message):
        return True

    # Check for an excessive use of special characters
    special_chars = re.findall(r'[*$%#!&()\[\]<>+^]', message)
    if len(special_chars) > 4:
        return True

    return False