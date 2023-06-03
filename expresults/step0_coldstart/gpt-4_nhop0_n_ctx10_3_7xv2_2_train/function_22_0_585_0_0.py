
import re

def is_spam(message):
    spam_patterns = [
        r"\d+%↑",                # percentage with up arrow
        r"추천주",                # stock recommendation
        r"혜택",                  # benefits
        r"무료거부",              # opt-out messages
        r"https://me2\.kr/\w+",  # suspicious URL
        r"체험반",                # experience group
        r"프로젝트",              # project
        r"잔고만들기",            # balance making
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    
    return False
