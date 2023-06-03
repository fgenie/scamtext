
import re

def is_spam(message):
    # Check for common spam patterns
    spam_patterns = [
        r"(\d+[일|%]\s*((알려드린)|추천)|종목)",
        r"(vip(투자반))",
        r"(시작)",
        r"(차별화\s*된\s*분석)",
        r"(4월|(세토피아))",
        r"(캐스트(리뉴얼))",
        r"((금일|오늘)\s*부터)",
        r"(많은\s*이용)",
        r"(분석\/추천\/시황)",
        r"(실력으로\s*입증)",
        r"(내일 오전(9시)|공시발표가)",
        r"(성과를 챙겨가십시오)",
        r"(목요일 공시발표가)",
        r"(\d+[월]\s*총\s*수익)",
    ]
    
    # Iterate through the patterns and check if any of them are in the message
    for pattern in spam_patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match: 
            return True
    
    # If none of the patterns matched, the message is considered not spam
    return False
