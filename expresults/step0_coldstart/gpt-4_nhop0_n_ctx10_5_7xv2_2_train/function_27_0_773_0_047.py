
import re

def is_spam(message):
    # Check for spam keywords and patterns in the message
    spam_patterns = [
        r"\b(광고|상한가|추천주|수익률|무료거부|최소.{0,5}연상|선취매|단체방|소외주|테마주|수급주)\b",
        r"\b([0-9]{2,5}원|%|이상|백만원)\b",
        r"\b(me2\.kr|[a-zA-Z0-9-]+\.com|bit\.ly|t\.ly|openkakao\.it)\b",
        r"openkakao\.it\/\w{3,5}",
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message, re.IGNORECASE | re.MULTILINE):
            return True

    return False
