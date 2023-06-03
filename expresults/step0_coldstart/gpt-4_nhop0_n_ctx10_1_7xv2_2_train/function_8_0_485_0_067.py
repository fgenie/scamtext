
import re

def is_spam(message):
    spam_keywords = [
        "님",
        "방입장",
        "수익",
        "회사공시",
        "고정수입",
        "목표가",
        "익 절 가",
        "수익률",
        "투자계획",
        "종목",
        "폭등확정",
        "정회원방",
        "고수익",
        "무료체험"
    ]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    url_pattern = r"https?://(?:www\.)?[\w.-]+(?:\.[\w\.-]+)+(?:[\w\!\.\*_-]+(?:/|\b))"
    urls = re.findall(url_pattern, message)

    if len(urls) > 1:
        return True

    return False
