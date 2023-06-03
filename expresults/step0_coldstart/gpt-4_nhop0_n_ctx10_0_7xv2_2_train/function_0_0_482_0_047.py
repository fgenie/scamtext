def is_spam(content):
    import re

    # Common spam indicators
    spam_indicators = [
        r"수익",
        r"익절",
        r"목표가",
        r"\d{1,2}차목표",
        r"투자자문",
        r"다음 타자는",
        r"거래소",
        r"종목 확인",
        r"특징주",
        r"주식",
        r"지긋지긋",
        r"공짜",
        r"게임",
        r"혜택",
        r"초대받지않았어",
        r"올인",
        r"지인추천 이벤트",
        r"체험",
        r"비과세",
        r"[^\w](F|f)[0-9]*",
        r"로봇사업",
        r"상장기업",
        r"준법감시인",
        r"신입",
        r"특선",
        r"이유는",
        r"산출물",
        r"광고",
    ]

    for indicator in spam_indicators:
        if re.findall(indicator, content.strip()):
            return True

    # Detect and eliminate URLs that may not be spam
    non_spam_urls_re = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    content_no_urls = re.sub(non_spam_urls_re, "", content)

    # If the content does not contain spam indicators but still contains URLs, flag it as spam
    if re.findall(r"(http|www)", content_no_urls.strip()):
        return True

    return False