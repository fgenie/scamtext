
import re

def is_spam(message: str) -> bool:
    # Check for common spam words and phrases
    spam_words = ["추천주", "체험", "공시발표", "목표달성", "수익", "투자", "증권", "정보방", "국내식약처", "안정적인 수익", "클릭", "금전요구", "상한가", "연매출", "매출", "무료거부", "총 수익", "위험", "특집", "국내", "상품안내", "알려드린", "출신"]

    for word in spam_words:
        pattern = re.compile(word)
        if pattern.search(message):
            return True

    # Check for shortened URLs and suspicious links
    url_regex = r"(?P<url>https?://\S*\.[\w]*(?=\s|\b))"
    urls = re.findall(url_regex, message)
    spam_urls = ["me2.kr", "bit.ly", "dokdo.in"]
    for url in urls:
        for spam_url in spam_urls:
            if spam_url in url:
                return True

    # Check for unusual numbers by looking for consecutive digits or percentage signs
    numbers_regex = r"\d{2,}|%"
    numbers = re.findall(numbers_regex, message)
    if numbers:
        return True

    return False
