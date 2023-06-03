
import re

def is_spam(message):
    spam_pattern = re.compile(r'([가-힣]*VIP체험반|[0-9]*억보증공원|[0-9]*%OK|▼확인▼|[0-9]*+치킨/매[0-9]*%|https://\S+|_url_here_)')

    if re.search(spam_pattern, message):
        return True
    else:
        return False
