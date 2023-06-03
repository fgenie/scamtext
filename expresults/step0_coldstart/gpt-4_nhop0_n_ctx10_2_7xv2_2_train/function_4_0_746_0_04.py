
import re

def is_spam(message):
    spam_keywords = [
        r'\bVIP',
        r'\bvip',
        r'\bhttp',
        r'\bhttps',
        r'bit\.ly',
        r'톡\w{2,}',
        r'원으로',
        r'주룩',
        r'클릭',
        r'타점',
        r'공개',
        r'출신',
        r'\d{2}월',
        r'##+#',
        r'회취킨',
        r'비공개정보방',
        r'알려드린',
        r'체험반',
        r'단독입수',
    ]

    message = message.replace('\n', ' ')
    message = re.sub(r'\s+', ' ', message)

    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    return False
