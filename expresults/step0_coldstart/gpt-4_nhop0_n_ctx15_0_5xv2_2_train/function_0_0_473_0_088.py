
import re

def is_spam(message: str) -> bool:
    # Check for common spam features like excessive use of special characters and numbers
    special_chars = "!@#$%^&*()_+-=[]{};:,./<>?"
    num_special_chars = sum(c in special_chars for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_alphas = sum(c.isalpha() for c in message)
    
    if num_special_chars > num_alphas / 3 or num_digits > num_alphas / 3:
        return True

    # Check for common spam phrases
    spam_phrases = ["클릭", "고속급등", "수익률", "적립금", "현금 지급", "주식", "투자", "예금", "종복", "펀드", "비공개", "매수", "실현수익률", "Secured by", "안내", "광고"]
    message_words = message.split()

    for phrase in spam_phrases:
        for word in message_words:
            if phrase in word:
                return True

    # Check for multiple links in the message
    links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(links) > 1:
        return True

    return False
