import re

def is_spam(message):
    
    spam_words = ["무료수신거부", "광고", "회원가입", "장담합니다", "채팅방", "일지후에", "공짜", "단독발표", "해외선물", "실시간", "확탈코스"]
    message = message.lower()

    # Check for spam-related keywords
    for keyword in spam_words:
        if keyword in message:
            return True

    # Check for suspicious links 
    if re.search(r"https?:\/\/\S+|\S+\.kr|\S+\.\w{2}", message):
        return True

    # No spam-indicating signs found
    return False