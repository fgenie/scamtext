def is_spam(message):
    import re
    spam_keywords = ["원 준비", "자동으로", "슈퍼개미", "신규가입", "채팅방", "오픈채팅방", "수익달성", "첫 입금", "구독", "참여", "공부방", "URL"]
    msg_lower = message.lower()

    if len(re.findall('http(s)?:\/\/\S+', msg_lower)) > 0: 
        return True

    for keyword in spam_keywords:
        if keyword.lower() in msg_lower:
            return True

    return False