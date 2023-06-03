
import re

def is_spam(message):
    # Look for spam-specific keywords and patterns in the message
    keywords = ["추천주", "지금 가입", "VIP", "돌파", "참여", "상한가확정", "청개구리VIP", "출신", "수익", "루멘스"]
    url_pattern = r"(https?://\S+|me2\.\S+|vo\.la/\S+|dokdo\.\S+)"
    spam_score = 0

    for keyword in keywords:
        if keyword in message:
            spam_score += 1

    if re.search(url_pattern, message):
        spam_score += 1

    return spam_score > 1 # If the spam_score is greater than 1, classify the message as spam
