
import re

def is_spam(text: str) -> bool:
    
    # Check for spam keywords
    spam_keywords = ["광고", "핫딜", "편지함으로", "지금 바로", "무료거부", "지원금", "안전거래", "입장코드", "추천주", "수익", "주식", "특별한 혜택"]
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    # Check for url patterns
    url_pattern1 = r"https?://[^\s]+"
    url_pattern2 = r"www\.[^\s]+"
    url_match1 = re.search(url_pattern1, text)
    url_match2 = re.search(url_pattern2, text)

    if url_match1 or url_match2:
        if "원" in text or "계약" in text or "시작" in text or "특별" in text:
            return True
    
    # Check for money and percentage patterns
    money_pattern = r"\d{1,3}(,\d{3})*(\.\d{2})?원"
    money_match = re.search(money_pattern, text)
    percentage_pattern = r"\d{1,3}(\.\d{1,2})?%"
    percentage_match = re.search(percentage_pattern, text)

    if money_match and percentage_match:
        return True

    return False
