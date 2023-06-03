
import re

def is_spam(message: str) -> bool:
    # Increase spam score if message contains certain patterns
    spam_score = 0
    spam_patterns = [
        r'\b무료\b',
        r'\b체험\b',
        r'\b모집\b',
        r'https?://\S+',
        r'\d{1,3}[,\.]\d{3}[%↑]',
        r'\d{1,3}[,\.]\d{6}',
        r'\bAI\b',
        r'\b자동\b',
        r'\b매매\b',
        r'\b달성\b',
        r'\b추천주\b',
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            spam_score += 1

    # Set threshold for spam classification
    spam_threshold = 1
    if spam_score >= spam_threshold:
        return True
    else:
        return False
