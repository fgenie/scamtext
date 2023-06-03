
import re

def is_spam(message):
    spam_keywords = ['회원님', '수익', '무료', '광고', '혜택', 'P', '%', '확정', '오전', '오후', '단타', '이벤트', '참여하세요', '지금 바로 시작하세요', '선착순', '후후']
    link_pattern = re.compile(r'(?:https?://|www[.])[^\s/]+[.](?:com|kr|net|org|co.kr)[^\s]*')
    message_keywords = message.split()

    if re.search(link_pattern, message):
        return True

    for keyword in message_keywords:
        if keyword in spam_keywords:
            return True

    return False
