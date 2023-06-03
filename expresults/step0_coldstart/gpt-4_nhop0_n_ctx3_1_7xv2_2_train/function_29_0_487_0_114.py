def is_spam(message: str) -> bool:
    import re

    # Check message length
    if len(message) > 100:
        return True

    # Check for suspicious phrases
    spam_phrases = ["추천주", "공개합니다", "폭등", "↑ 돌파", "공시발표", "실력입증", "다음주도 이어서 나갑니다"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for multiple URL shorteners
    url_shorteners = re.findall(r'https?://\S+', message)
    if len(url_shorteners) > 1:
        return True

    # Check for special characters
    special_characters = re.findall(r'[<>%^*▲▼]', message)
    if len(special_characters) > 1:
        return True

    # If none of the above conditions are true, it is not spam
    return False