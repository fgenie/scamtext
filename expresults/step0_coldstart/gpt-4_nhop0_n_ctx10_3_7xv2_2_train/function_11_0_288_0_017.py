def is_spam(message: str) -> bool:
    import re

    # Check for common spam phrases or patterns
    spam_phrases = ['상한가', '실력입증', '추천주', '무료체험', '수신거부', '◆ 아래링크 클릭후 입장 ◆', '반등 구간', '테마주', '수급주']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for links and count them
    links_pattern = r'http(s)?://\S+'
    links = re.findall(links_pattern, message)
    if len(links) >= 2:
        return True

    # Check for multiple common spam punctuation
    if '!!' in message and '??' in message:
        return True

    # Check for excessive special characters
    special_chars = ['%', '▼', '▲', '*', '+', '↑', '▶']
    count = 0
    for char in special_chars:
        count += message.count(char)
    if count >= 5:
        return True

    return False