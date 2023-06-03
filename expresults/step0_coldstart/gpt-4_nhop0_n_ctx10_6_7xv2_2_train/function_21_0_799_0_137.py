
import re

def is_spam(message: str) -> bool:
    # Check for common spam keywords and phrases
    spam_keywords = ["수익", "체험반", "단독입수", "추천", "시황", "목표달성", "최소", "공개", "만원", "종목"]
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Check for presence of URLs/links
    url_pattern_1 = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    url_pattern_2 = r"me2\.kr/[a-zA-Z0-9]+"
    if re.search(url_pattern_1, message) or re.search(url_pattern_2, message):
        return True

    # Check for excessive use of punctuation
    excessive_punctuation = r"([,.!?:;]){2,}"
    if re.search(excessive_punctuation, message):
        return True
    
    return False
