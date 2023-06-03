
import re

def is_spam(text):
    # check for excessive use of special characters or numbers
    special_chars = r"[※광고``!@%$^&*+=(){}<>?=|''\’/’""';:'₩~`]"
    if len(re.findall(special_chars, text)) > 3:
        return True

    # check for repeated letters
    if re.search(r"(.)\1{2,}", text):
        return True

    # check if the message contains specific spam terms in lower case
    spam_terms = [
        "추천", "적중", "목표달성", "↑", "↓", "적중", "폭등", "성투", "투자", "종목", "공시공개", "최소", "이상상승", "클릭"
    ]
    text_lower = text.lower()

    for term in spam_terms:
        if term in text_lower:
            return True

    # check for shortened URLs
    short_urls = [
        r"https?://bit\.ly/\S+",
        r"https?://goo\.gl/\S+",
        r"https?://me2\.kr/\S+",
        r"https?://vo\.la/\S+",
        r"https?://kakaotalk\.at/\S+",
        r"https?://asq\.kr/\S+",
        r"https?://han.gl/\S+"
    ]

    for url in short_urls:
        if re.search(url, text):
            return True

    return False
