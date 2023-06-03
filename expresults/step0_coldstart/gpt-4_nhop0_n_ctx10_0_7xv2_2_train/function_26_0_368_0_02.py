
import re

def is_spam(message: str) -> bool:
    # Patterns and keywords that might indicate spam messages
    spam_patterns = [
        r"https?://",  # URLs
        r"회원님",  # Addressing the user in a formal way
        r"카톡방",  # Mentioning KakaoTalk chat rooms
        r"상한가",  # Stock price up limit
        r"수익률",  # Profit rate
        r"\d{2,3}%\↑",  # Percentage increases in stock prices
        r"\d{1,2}일",  # Days of the month
        r"\d{1,2}시",  # Hours of the day
        r"\(광고\)",  # Advertising label
        r"무료수신거부",  # Opt-out message for free
        r"무료거부",  # Opt-out message for free (alternative)
    ]
    num_spam_patterns = sum([bool(re.search(pattern, message)) for pattern in spam_patterns])
    
    # Set a threshold for the sum of matched patterns to classify the message as spam
    spam_threshold = 2
    
    return num_spam_patterns >= spam_threshold
