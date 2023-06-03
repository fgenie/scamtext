def is_spam(message: str) -> bool:
    import re

    # Check for common phrases in spam messages
    spam_phrases = ["공개", "최종논의단계", "최소", "적중", "실력입증", "추천주"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r'https?://\S+')
    if url_pattern.search(message):
        return True

    # Check for excessive usage of special characters
    special_chars_pattern = re.compile(r'[-!$%^&*()_+|~=`{}\[\]:";<>?,./]')
    if len(special_chars_pattern.findall(message)) >= 3:
        return True

    # If none of the above conditions are met, the message is considered normal
    return False