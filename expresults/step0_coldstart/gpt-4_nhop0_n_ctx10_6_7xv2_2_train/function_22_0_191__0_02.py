
import re

def is_spam(message: str) -> bool:
    """
    Simple function to classify the given message as spam or not

    :param message: The text message to be classified as spam or not
    :return: True if the message is spam and False otherwise
    """
    spam_keywords = [
        "무료 상담 문의",
        "목표달성기념",
        "추천 디젠스",
        "편리한 자동진행",
        "주 15,130,000원 마감",
        "알려드린 세토피아 축하",
        "여의도4월체험반 다음 타자는",
        "개장전 체크하세요",
        "최소 금요일 20%",
        "회사공시 발표",
        "전문가 경력",
        "실전투자대회 top10",
        "누적수익률",
        "종목 적중하여 좋은결과",
        "300~400% 자신",
        "클릭 종목확인",
        "지금 주식 수익률대회",
        "익 절 가"
    ]

    url_regex = r'(?:http|ftp|hxxp|ftpx|https)://(?:[^\s\xa0<>]+)'

    for keyword in spam_keywords:
        if keyword in message:
            return True
        
    spam_url_count = len(re.findall(url_regex, message))
    if spam_url_count >= 2:
        return True

    return False
