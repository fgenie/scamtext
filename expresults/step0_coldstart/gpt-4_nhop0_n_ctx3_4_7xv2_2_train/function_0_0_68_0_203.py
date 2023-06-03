def is_spam(message: str) -> bool:
    import re

    # Define patterns that might indicate a spam message
    spam_patterns = [
        r'\d{1,2}월',  # Find digits followed by '월' character
        r'https?',
        r'[ㄱ-ㅎㅏ-ㅣ]',  # Consecutive Korean jamo characters
        r'▲|▼',
        r'[!()\-#]',  # Excessive punctuations
        r'\d{3,}/\d{3,}',  # Large, consecutive numbers separated by a slash
    ]

    # Combine the patterns
    combined_patterns = "|".join(spam_patterns)
    spam_regex = re.compile(combined_patterns)
    found_spam = spam_regex.findall(message)

    # If at least one of the patterns is found in the message, classify it as spam
    if len(found_spam) > 1:
        return True

    return False