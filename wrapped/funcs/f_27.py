
import re

def is_spam(text):
    # Check for specific keywords
    keywords = ["광고", "무료거부", "긴급", "핵심정보", "프로젝트", "추천주", "지금 바로", "수익률", "입금"]
    if any(keyword in text for keyword in keywords):
        return True
    
    # Check for urls with suspicious patterns
    urls_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(urls_pattern, text)
    if urls:
        for url in urls:
            if any(word in url for word in ["bit.ly", "me2.kr", "오픈톡"]):
                return True

    # Check for consecutive digits or percentages
    digits = re.findall(r'\d{3,}', text)
    percentages = re.findall(r'\d{2,}%+', text)
    if digits or percentages:
        return True

    # Check for multiple special characters
    special_chars = re.findall(r'[\*-_@.&+:]+', text)
    if len(special_chars) > 2:
        return True

    return False
