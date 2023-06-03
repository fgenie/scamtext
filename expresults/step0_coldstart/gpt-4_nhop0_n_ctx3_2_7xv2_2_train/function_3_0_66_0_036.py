
import re

def is_spam(message):
    # Check for presence of URLs
    url_pattern = re.compile(r'(https?://\S+)')
    if url_pattern.search(message):
        return True

    # Check for suspicious keywords
    spam_keywords = ['축하합니다', '알려드린', '체험반', 'VIP', '투자반', '차별화 된', '분석/추천/시황', '실력으로 입증', '비공개정보방', '매수매도타점공유', '참가']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Return False if no spam indicators are found
    return False
