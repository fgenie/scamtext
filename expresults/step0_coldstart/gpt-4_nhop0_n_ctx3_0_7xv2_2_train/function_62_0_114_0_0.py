import re

def is_spam(text):
    # Check for suspicious content
    spammy_phrases = [
        '안녕하세요 당첨 되셨습니다',
        '귀하의 투자계획은',
        '손 놓고 있으실 건가요',
        '재할 성과',
        '무료번호이벤트',
        '배움의길',
    ]
    
    links_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

    for phrase in spammy_phrases:
        if phrase in text:
            return True

    # Check for excessive URLs
    urls = re.findall(links_pattern, text)
    if len(urls) >= 2:
        return True

    return False