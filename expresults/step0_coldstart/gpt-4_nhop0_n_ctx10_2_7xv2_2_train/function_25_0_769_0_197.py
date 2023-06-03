
import re

def is_spam(message):
    # Convert the message to lowercase
    message = message.lower()
    
    # Check for typical spam-related phrases and patterns
    spam_phrases = [
        r"이게 뭐지",
        r"% 확정",
        r"상승 확정",
        r"무조건 올라갑니다",
        r"최대 \d+% 할인",
        r"클릭",        r"https://me2.kr/\w+",
        r"익절",
        r"수익",
        r"상한가",
        r"메아리 시작합니다\.",
        r"후회 없으실",
        r"어떻게해서 만들수 있었을까요\?",
    ]

    for spam_phrase in spam_phrases:
        if re.search(spam_phrase, message):
            return True
    
    # Check for excessive use of special characters
    special_chars = "!.?*"
    special_char_count = sum(message.count(c) for c in special_chars)
    if special_char_count / len(message) > 0.1:
        return True

    # Check for excessive use of numbers
    number_count = sum(c.isdigit() for c in message)
    if number_count / len(message) > 0.1:
        return True
       
    return False
