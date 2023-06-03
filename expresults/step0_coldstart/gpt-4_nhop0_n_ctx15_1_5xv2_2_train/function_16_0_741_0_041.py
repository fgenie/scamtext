
import re

def is_spam(message):
    # Find patterns commonly found in spam messages
    patterns = [
        r'(광고)',  # Advertising in Korean
        r'https?://\S+',  # URLs
        r'\b[백만천만만억]+원?\b',  # Large amount of money in Korean
        r'[%][0-9]+',  # Percentage
        r'\b지원\b',  # Support in Korean
        r'\b수익\b',  # Profit in Korean
        r'\b주식\b',  # Stock in Korean
        r'\b어디서 만나\??\b',  # Where to meet in Korean
        r'\b청개구리\b',  # Frog in Korean
        r'\b투자\b',  # Investment in Korean
        r'\b정보\b',  # Information in Korean
        r'\b초대\b',  # Invitation in Korean
    ]

    spam_score = 0

    for pattern in patterns:
        if re.search(pattern, message):
            spam_score += 1

    # If spam_score is greater or equal to 1, it is considered spam
    if spam_score >= 1:
        return True
    else:
        return False
