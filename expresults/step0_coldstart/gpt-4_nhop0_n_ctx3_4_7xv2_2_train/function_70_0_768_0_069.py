def is_spam(message):
    import re

    # Check if the message is an advertisement
    if re.search(r'\(광고\)', message):
        return True

    # Check for common spam phrases or patterns
    spam_phrases = [
        r'투자', r'수익', r'부자', r'노하우', r'공개공부', r'% 달성',
        r'오픈채팅방', r'https?://\S+', r'무료수신거부', r'무료거부',
        r'최대 \d+% 할인', r'EVENT 진행', r'code :', r'상승'
    ]
    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    # If none of the above conditions are met, the message is not spam
    return False