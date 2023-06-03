
import re

def is_spam(message):
    # define regex pattern to identify links
    link_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    
    # check if message contains a link
    if link_pattern.search(message):
        # check if message is a spam message by checking key words
        spam_keywords = ['VIP', '추천', '안전', '체험반', '당첨', 'VVIP', '기회', 
                         '확률', '카톡방', '정회원', '적중', '감사합니다']
        for keyword in spam_keywords:
            if keyword in message:
                return True
        return False
    else:
        return False
