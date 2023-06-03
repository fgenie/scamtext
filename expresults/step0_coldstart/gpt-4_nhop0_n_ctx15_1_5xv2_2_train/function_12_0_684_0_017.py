
import re

def is_spam(message):
    # Patterns that can indicate a message is spam
    spam_words = ['축하합니다', '공개합니다', '\\d{1,2}일추천', '알려드린', '무료체험', '돌파', '상한가', '최소.*연상']
    url_shorteners = ['bit.ly', 'me2.kr', 'han.gl']
    consecutive_numbers = '\\d+\\.?\\d*'  # e.g., 30%, 19일
    suspicious_referral = '\\d{1,2}[일월수목금토일]'

    # Flags for checking whether a message is spam
    contains_spam_word = any(re.search(word, message) for word in spam_words)
    contains_short_url = any(short_url in message for short_url in url_shorteners)
    contains_consecutive_numbers = re.search(consecutive_numbers, message)
    contains_suspicious_referral = re.search(suspicious_referral, message)

    # Evaluate if message is a spam based on the flags
    if contains_spam_word and contains_short_url:
        return True
    if contains_consecutive_numbers and contains_suspicious_referral:
        return True
    if contains_spam_word and contains_consecutive_numbers:
        return True
    if contains_spam_word and contains_suspicious_referral:
        return True
    if contains_short_url and (contains_consecutive_numbers or contains_suspicious_referral):
        return True

    # If none of the conditions are met, return False, indicating the message is not spam
    return False
