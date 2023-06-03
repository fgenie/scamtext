def is_spam(message: str) -> bool:
    import re

    keywords = ['악성광고', '텔레그램', '이동합니다', '기존 정보', '혜택', '마지막반', '잔여', 'https://', '축하합니다', '월체험']
    
    # Checks for Korean specific keywords
    if any(keyword in message for keyword in keywords):
        return True

    # Check for excessive numbers or special characters in the message
    num_special_characters = len(re.findall("[^a-zA-Z0-9가-힣\s]+", message))
    if num_special_characters / len(message) > 0.1:
        return True

    # Check for excessive capitalization or white spaces in the message
    num_uppercase = sum(c.isupper() for c in message)
    num_whitespace = message.count(' ')
    text_length = len(message)
    if (num_uppercase / text_length > 0.6) or (num_whitespace / text_length > 0.5):
        return True

    return False