
import re

def is_spam(text):
    spam_keywords = ["마감임박", "긴급히 연락", "공시 종목", "빠른 확인", "매수세 포착", "출금 10만", "차별화된 전략", "이 회사는 목요일 공시발표가", "클릭후 입장",
                    "내일 오전 9시에", "현직국 회의원", "장담합니다", "출금 10만OK", "어디쯤 오고 있어? ", "신규 30,000원"]

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    if len(urls) > 0:
        for url in urls:
            if "mpp23.com" in url or "openkakao.it" in url:
                return True

    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False
