
import re

def is_spam(message: str) -> bool:
    spam_keywords = [
        r'광고', r'체험반', r'수익', r'안전하고', r'상한가확정',
        r'회원', r'자산관리', r'무료거부', r'비용', r"성과",
        r"계약", r'추천', r'다음타자', r'느\r\n'
    ]
    
    suspicious_keywords = [
        r'https?://\S+', r'\d{4}', r'계\.\s?약\.\s?기준'
    ]
    
    spam_score = 0

    for keyword in spam_keywords:
        if re.search(keyword, message):
            spam_score += 1
    for keyword in suspicious_keywords:
        if re.search(keyword, message):
            spam_score += 0.5

    return spam_score > 2

