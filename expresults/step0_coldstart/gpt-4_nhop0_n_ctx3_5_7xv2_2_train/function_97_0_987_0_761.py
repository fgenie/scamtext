
import re

def is_spam(message):
    # Check for unusual patterns and characters
    if re.search(r'[ㄱ-ㅎ가-힣0-9]{3,}', message):
        return True

    # Check for percentage signs, discount offers and URLs
    if re.search(r'(매\d{1,2}%|BBQ|승인전화|bit\.ly|\bKEY:|https?:\/\/\S+)', message, re.IGNORECASE):
        return True

    # Check for event dates and announcements
    if re.search(r'(\d{1,2}일 알려드린 세토피아|파이널VIP체험반 \d{1,2}(월)시작)', message):
        return True

    # If none of the above conditions are met, the message is not spam
    return False
