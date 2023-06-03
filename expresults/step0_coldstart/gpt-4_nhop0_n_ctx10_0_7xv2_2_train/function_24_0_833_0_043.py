
import re

def is_spam(message):
    spam_keywords = ["추천주", "상담하기", "클릭", "축하합니다", "%↑", "여의도", "가격", "목표가", "월체험반", "작전정보", "VIP", "공시", "추천종목", "투자체험", "폭등", "계획", "체험반", "공유", "기법", "아줌마", "비결", "단타", "매수/매도타점", "(광고)", "기대하셔도좋고", "공시발표", "확실하게 가겠습니다", "무료거부"]
    message = message.lower()

    if "http" in message or "https" in message:
        url_reg = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        urls = re.findall(url_reg, message)
        if len(urls) > 0:
            return True

    for keyword in spam_keywords:
        if keyword.lower() in message:
            return True

    if "서울파이낸스기자 김동진입니다" in message:
        return True

    if re.search(r"[0-9,]{3,}원", message):
        return True

    return False
