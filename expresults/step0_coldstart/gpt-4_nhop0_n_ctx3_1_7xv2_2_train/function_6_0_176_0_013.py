
import re

def is_spam(message: str) -> bool:
    # Patterns indicating a spam message
    patterns_to_look = [
        r'https?:\/\/\S+', # URLs
        r'상한가|제휴협약|발표시|단독제휴|신청하신|적중', # Spam-related words
        r'[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}', # domain-like strings
    ]

    for pattern in patterns_to_look:
        matches = re.findall(pattern, message)
        if matches:
            spam_score = len(matches)
            if spam_score > 1:
                return True

    return False
