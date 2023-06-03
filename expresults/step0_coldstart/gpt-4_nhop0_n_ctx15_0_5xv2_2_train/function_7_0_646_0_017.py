
import re

def is_spam(message):
    spam_phrases = [
        'VIP투자반', '악성광고', '추천', '공개', '상장스타트업', '실력입증',
        '수익률', '증권사부장출신', '종목상담', '국내식약처', '매주BBQ', '승인전화',
        '선물매매', '송', '노출', 'FDA승인'
    ]
    
    shortcut_links_regex = r"me2\.kr\/[a-zA-Z0-9]+|bit\.ly\/[a-zA-Z0-9]+|t.ly\/[a-zA-Z0-9]+"
    links = re.findall(shortcut_links_regex, message)

    if links:
        return True

    for phrase in spam_phrases:
        if phrase in message:
            return True

    return False
