
import re

def is_spam(message):
    # Check for common spam indicators in the message
    if re.search(r'(광고|\bclick\b|축하|상한가|종목|주식|투자|환전|강력추천|카>에볼|쿠폰|결제| 비용요구|\bhttps?://|폭등|모집|안내)', message, re.IGNORECASE):
        return True
    else:
        return False
