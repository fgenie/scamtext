
import re

def is_spam(text):
    # Check for URL pattern
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urls = url_pattern.findall(text)
    
    # Check for non-Korean characters and non-alphanumeric pattern
    non_kor_pattern = re.compile(r'[^\uac00-\ud7a3\s\w\!\?\.,]+')
    non_kor = non_kor_pattern.findall(text)
    
    # Calculate the ratio of non-Korean characters to total text length
    non_kor_ratio = sum(len(match) for match in non_kor) / len(text) if text else 0

    # Check if the message contains invite-related keywords
    invite_words = ["정회원방", "체험", "고수익", "Vip방", "잔여"]
    invite = any(word in text for word in invite_words)

    # Classify as spam based on the presence of a URL, high non-Korean ratio or invite-related keywords
    return (len(urls) > 0) or (non_kor_ratio > 0.5) or invite
