
import re

def is_spam(text):
    # Check for spam keywords and URL patterns
    spam_keywords = ["미래가 달라집니다", "주종/시황/뉴스", "비번:", "차별화 된 분석/추천/시황", "실력으로 입증", "지난주 추천주 현황", "정확한 분석/타점",
                     "검증된 수익률", "종목상담/추천", "무 료 체 험", "자 동 매 매"]
    spam_url_patterns = [r'https?://bit\.ly/\S+', r'https?://me2\.kr/\S+', r'https?://ko\.gl/\S+']

    for keyword in spam_keywords:
        if keyword in text:
            return True

    for pattern in spam_url_patterns:
        if re.search(pattern, text):
            return True

    return False
