
import re

def is_spam(message):
    spam_keywords = ['가입', '목표달성', '추천', '종목', 'VIP', '투자반', '시황']
    url_pattern = r'(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'

    if re.search(url_pattern, message) and any(keyword in message for keyword in spam_keywords):
        return True
    else:
        return False
