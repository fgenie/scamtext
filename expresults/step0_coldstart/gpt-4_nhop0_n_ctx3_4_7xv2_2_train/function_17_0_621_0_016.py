
import re

def is_spam(message: str) -> bool:
    # Define spam pattern
    spam_pattern = [
        r"(목표가|현재가격|누적수익률|달성|추천)",
        r"(익 명 받은|서울경제팍TV|전문애널리스트|금전적인 요구)",
        r"(openkakao\.at|me2\.kr)",
        r"(유\.료|무료입장|수\.익)"
    ]
    
    # Check if the pattern is in the message
    for pattern in spam_pattern:
        if re.search(pattern, message, flags=re.IGNORECASE | re.MULTILINE):
            return True

    # Otherwise, it's not spam
    return False
