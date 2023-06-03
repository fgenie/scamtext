
import re

def is_spam(message):
    spam_phrases = [
        r"(?i)(\d+\s*원)",  # Price in won
        r"(?i)(\d+%(\s)?↑)",  # Percentage rise with arrow
        r"(?i)(매수세|파는|매수)(\w|\W)*",  # Keywords related to buying and selling
        r"(?i)(추천|고급정보|투자|기회)",  # Spammy terms
        r"(?i)(bit\.ly|me2\.kr|tuney\.kr|openkakao\.it)",  # Spammy URL shorteners
        r"(?i)(무료상담|무료체험|목표달성)",  # Free consultation, free trial, target achieved
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True
    return False
