
import re

def is_spam(message: str) -> bool:
    message = message.lower()
    message_words = re.findall(r'\w+', message)
    
    # Check for suspicious URL patterns
    suspicious_urls = r'(https?:\/\/me2\.kr\/[\w-]+|openkakao\.io\/[\w-]+)'
    if re.search(suspicious_urls, message):
        return True

    # Check for restricted words related to spam
    spam_words = ["체험반", "추천주", "축하합니다", "알려드린", "종목추천", "종목상담", "광고", "진입 예정", "지원금", "무료거부", "공개정보", "vip체험반", "적중", "매수매도타점공유", "참가"]
    for word in spam_words:
        if word.lower() in message_words:
            return True

    # Check for suspicious patterns in message content
    spam_patterns = [r'[\w\s-]*\d{1,2}일[\s\W]*', r'월공개', r'목표달성기념', r'금일 [\d\s]*시', r'\d일 발표예정정보', r'4월체험', r'각칸의']
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If none of the above conditions are met, consider the message normal
    return False

