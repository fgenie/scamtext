
import re

def is_spam(message):
    spam_keywords = ["무료체험반", "증권", "VIP", "고급 정보", "상승", "익절", "오픈", "상한가", "와이투솔루션", "지원금", "출금가능", "투자", "성과", "예상", "수급"]

    message = message.lower()
    
    if any(re.search(r'\b' + keyword.lower() + r'\b', message) for keyword in spam_keywords):
        return True
    else:
        return False
