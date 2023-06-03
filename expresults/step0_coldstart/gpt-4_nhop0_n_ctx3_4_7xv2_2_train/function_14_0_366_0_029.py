
import re

def is_spam(message: str) -> bool:
    # Checking for spam indicators in the message
    message = message.lower()
    spam_indicators = [
        r"\d{1,}%\s*↑",  # percentages followed by upward arrows
        r"\d{1,}\s*%(\s*이상)?\s*(상승|익절)",  # percentages with mentions of increase or profit
        r"무료",  # mention of "free"
        r"비용없",  # mention of "no cost"
        r"최소\s*\d{1,}%\s*이상",  # mention of "at least X%"
        r"상한가달성",  # mention of "upper limit"
        r"공시발표",  # mention of "public announcement"
        r"폭등",  # mention of "sharp rise"
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    return False
