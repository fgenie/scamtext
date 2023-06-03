
import re

def is_spam(message):
    spam_keywords = ["루멘스", "엠바고", "정식허가임박", "상한가", "S전자", "계열사합병", "FROG", "축하합니다", "체험반", "퍼.센.트", "참여하기", "무료체험", "오픈하겠습니다", "폭등예상", "장기적으로", "따라서", "광고"]

    message = message.lower()

    for keyword in spam_keywords:
        keyword = keyword.lower()
        if keyword in message:
            return True

    url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    url_count = len(re.findall(url_regex, message))

    if url_count >= 2:
        return True

    return False
