
import re

def is_spam(message: str) -> bool:
    # Check for common spam phrases
    spam_phrases = ["광고", "지원금", "무료거부", "상품권", "비밀번호", "구매하세요", "마감", "혜택", "카톡방", "차 몰래 뒤에 따라올게", "전문가"]
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for URLs and codes
    url_regex = r'(https?:\/\/)?\S*(?:\.\S*)+\S*'
    url_match = re.search(url_regex, message)
    code_regex = r'코드:\d+'
    code_match = re.search(code_regex, message)
    if url_match or code_match:
        return True
    
    # Check for continuous repetition of capital or lowercase letters
    letter_repetition_regex = r'([A-Za-z])\1{2,}'
    letter_repetition_match = re.search(letter_repetition_regex, message)
    if letter_repetition_match:
        return True
    
    return False
