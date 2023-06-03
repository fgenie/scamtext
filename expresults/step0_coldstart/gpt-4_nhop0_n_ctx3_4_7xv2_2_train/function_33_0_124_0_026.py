
import re

def is_spam(message):
    spam_indicators = [
        r"\b(광고)\b",
        r"\b(출시 이벤트)\b",
        r"\b(해외선물)\b",
        r"\b(수익실현)\b",
        r"\b(무료거부)\b",
        r"\b(입장번호)\b",
        r"\b(챗 GPT)\b",
        r"\b(학습)\b",
    ]
    
    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True
            
    return False
