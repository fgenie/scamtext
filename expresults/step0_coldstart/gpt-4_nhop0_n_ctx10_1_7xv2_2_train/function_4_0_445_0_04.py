
import re

def is_spam(message):
    # Convert the message to lowercase for consistent checking
    lower_message = message.lower()
    
    # Check for spam keyword indicators
    spam_indicators = [
        "체험반", "수익률", "종목상담", "게임정보", "무료거부",
        "추천주", "상한가확정", "고정수입", "광고"
    ]
    for keyword in spam_indicators:
        if keyword in lower_message:
            return True
            
    # Check for spam characteristics
    urls_count = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', lower_message))
    excessive_punctuation = re.search(r"[.?!]{3,}", lower_message)
    
    if urls_count >= 2 or excessive_punctuation:
        return True
    
    return False
