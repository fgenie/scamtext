
import re

def is_spam(message):
    # Check for URL indicators in the spam message examples
    url_pattern = r"(http|https|openkakao)([^\s]+)"
    url_result = re.search(url_pattern, message)
    
    # Check for non-Korean/English characters
    non_kor_eng_pattern = r"[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\s]+"
    non_kor_eng_result = re.search(non_kor_eng_pattern, message)

    # Check for money or percentage symbols
    money_pct_pattern = r"(\d+%|\d+원|\d+퍼)"
    money_pct_result = re.search(money_pct_pattern, message)
    
    # If any of the above patterns match, then the message is likely spam
    if url_result or non_kor_eng_result or money_pct_result:
        return True
    
    return False
