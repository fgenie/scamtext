
import re

def is_spam(text: str) -> bool:
    spam_keywords = ['상한가', '추친중', '무료체험', '수익보장', '정보입수', '출발', '마감', '무료거부', '코드', '체험반', '초대', '실력입증', '알려드린', '카카오톡제재']
    suspicious_url_pattern = r'(https?://[^\s]+)'
    suspicious_url_pattern2 = r'(han.gl/[^\s]+)'

    found_keyword = any(word in text for word in spam_keywords)
    found_suspicious_url = re.search(suspicious_url_pattern, text) or re.search(suspicious_url_pattern2, text)

    if found_keyword or found_suspicious_url:
        return True
    
    return False
