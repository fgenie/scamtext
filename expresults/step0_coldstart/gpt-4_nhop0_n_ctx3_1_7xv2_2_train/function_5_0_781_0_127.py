def is_spam(message: str) -> bool:
    import re

    # Check for multiple consecutive exclamation points or question marks
    if re.search(r'(!|\?){2,}', message):
        return True

    # Check for common spam phrases
    spam_phrases = ["상한가", "목표가", "클릭후무료입장", "openkakao", "me2.kr", "당첨 되셨습니다", "유.료 전환"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for consecutive uppercase words
    if re.search(r'\b([A-Z]+)\b(?:[^\w]*\s+\b([A-Z]+)\b)+', message):
        return True

    # Check for multiple numbers 
    if len(re.findall('\d+', message)) > 3:
        return True

    # If none of the conditions are met, the message is likely not spam
    return False