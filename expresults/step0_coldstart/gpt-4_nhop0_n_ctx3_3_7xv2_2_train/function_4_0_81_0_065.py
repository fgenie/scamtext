
import re

def is_spam(text):
    # Check for common spam terms and phrases
    spam_terms = ["광고", "추천", "투자", "매집", "특별한 기회", "단기트레이딩", 
                "2차전지", "500% 이상 수익", "거래대금", "적정 주가의 위치", "재료의 강도", "적정 주가의 위치"]
    
    # Check for URLs and shortlinks
    url_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    shortlink_regex = re.compile(r"(t[.]ly|bit[.]ly|go[.]gl|me2[.]kr)/\S+")

    # Check for any spam terms
    for term in spam_terms:
        if term in text:
            return True

    # Check for URLs
    url_search = url_regex.search(text)
    if url_search:
        return True

    # Check for shortlinks
    shortlink_search = shortlink_regex.search(text)
    if shortlink_search:
        return True

    # If no spam-like characteristics found, then the message is not spam
    return False
