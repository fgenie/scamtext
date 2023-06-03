
import re

def is_spam(message):
    # Define spam indicators
    spam_indicators = [
        "상한가",
        "비용",
        "수익",
        "무료거부",
        "약속",
        "선착순",
        "입장",
        "관망",
        "투자",
        "경제",
        "K B",
        "특별",
        "평생무상",
        "실력",
        "계약",
        "해선",
        "http(s)?\\W",
        "\d{4}\W",
    ]
    
    # Compile indicators into a regex pattern
    pattern = re.compile("|".join(spam_indicators), re.IGNORECASE)
    
    # Search for spam indicators in the message
    if pattern.search(message):
        return True
    else:
        return False
