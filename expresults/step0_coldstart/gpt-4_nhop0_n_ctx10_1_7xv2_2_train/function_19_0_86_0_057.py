
import re

def is_spam(message):
    # General spam indicators
    spam_indicators = [
        r'https?://\S+',  # URLs
        r'\d{1,2}월\d{1,2}주차',  # Month and week pattern (e.g. 4월3주차)
        r'\d{1,2}(\.\d{1,2})?%|%/[\d\.,]*',  # Percentage pattern (e.g. 42% or 3o ％)
        r'bit\.ly|me2\.kr|kk?talk|.naver|.com',  # Shortened URLs and some common domains
        r'●|▲|▼|※|■',  # Uncommon symbols often used in spams
        r'입력코드|톡|[KEY|key]:\d{4}',  # Indicators of chatting app, codes
        r'VIP|체험반|취킨|올인',  # Common spam words
        r'\d{1,2}일',  # Date pattern(e.g. 17日)
    ]
    
    # See if any spam indicators are found in the message
    for spam_indicator in spam_indicators:
        if re.search(spam_indicator, message):
            return True

    return False
