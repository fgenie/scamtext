
import re

def is_spam(message):
    # Check for common spam characteristics
    if re.search(r"\d{1,3}(,\d{3})*(\.\d{1,2})?->(\d{1,3})(,\d{3})*(\.\d{1,2})?", message):
        return True
    if re.search(r"https?://\S+", message) and re.search(r"(?i)(VIP|체험반|시작|종목|명가)", message):
        return True
    if re.search(r"(?i)(월)시작|공시|단독입수", message) and not re.search(r"(?i)([A-Za-z])", message):
        return True
    if re.search(r"(?i)(쉬는시간|휴대폰만|있으면)", message):
        return True
    
    # If none of the spam characteristics are found, consider it a normal message
    return False
