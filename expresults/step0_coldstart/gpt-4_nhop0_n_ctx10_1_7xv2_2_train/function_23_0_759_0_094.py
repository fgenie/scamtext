
import re

def is_spam(message: str) -> bool:
    # Rule 1: Check for typical spam link patterns
    link_pattern = re.compile(r"((?:https?|ftp)://|(?:www|ftp)\.)[a-z0-9-]+(\.[a-z0-9-]+)+(/[^/]+)*/?\??[^/]+")
    if link_pattern.search(message):
        return True
    
    # Rule 2: Check for unusual number of special characters
    special_chars_percentage = sum(c.isalnum() for c in message)/len(message)
    if special_chars_percentage < 0.5:
        return True
    
    # Rule 3: Check for typical spam words
    spam_words = ["상한가확정", "VIP정보방", "AI사업본격화", "실력입증", "오픈합니다", "M반도체", "기술특허임박", "기존대비", "입증", "추천", "수익률", "동향", "적중"] 
    for spam_word in spam_words:
        if spam_word in message:
            return True

    # Rule 4: Check for excessive repetition of characters
    repeat_pattern = re.compile(r"(.)\1{2}")
    if repeat_pattern.findall(message):
        return True

    return False
