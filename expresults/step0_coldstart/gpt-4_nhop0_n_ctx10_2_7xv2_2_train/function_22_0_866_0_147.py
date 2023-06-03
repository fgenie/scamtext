
import re

def is_spam(message):
    # Check for common spam patterns such as URL shorteners, suspicious characters and phrases, and excessive punctuation
    url_shorteners = r'(bit\.ly|me2\.kr|ko\.gl|han\.gl|goo\.gl|ow\.ly|tinyurl)'
    suspicious_chars = r'[%$*&£#:!]+'
    common_spam_phrases = r'(최대수혜주|투자MOU|상한가|적립금|바\[CA\]|차별화 된|손실보상|신용평점이하락|즉시할인|적립금|혜택|공시|오픈)|(실력입증|전용|프로그램|추천주|이벤트|혜택|무료거부)'

    contains_url_shortener = bool(re.search(url_shorteners, message, flags=re.IGNORECASE))
    contains_suspicious_chars = bool(re.search(suspicious_chars, message))
    contains_spam_phrases = bool(re.search(common_spam_phrases, message, flags=re.IGNORECASE))

    # If message matches any of the patterns, classify it as spam
    return contains_url_shortener | contains_suspicious_chars | contains_spam_phrases
