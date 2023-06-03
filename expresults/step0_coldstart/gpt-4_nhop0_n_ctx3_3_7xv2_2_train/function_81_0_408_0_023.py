
import re

def is_spam(message):
    spam_keywords = ["매수", "기업세력", "종목", "수익", "오픈카톡", "폭등", "선별"]

    spam_pattern = re.compile("|".join(spam_keywords))
    has_spam = bool(spam_pattern.search(message))

    return has_spam
