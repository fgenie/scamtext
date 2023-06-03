
import re

def is_spam(message):
    # define patterns for spam
    spam_patterns = [
        "(\W|^)EVENT(\W|$)",
        "(\W|^)공지(\W|$)",
        "(\W|^)광고(\W|$)",
        "(\W|^)무료(\W|$)",
        "(\W|^)모집(\W|$)",
        "(\W|^) 상승!(\W|$)",
        "(\W|^) 체험반(\W|$)",
        "(\W|^)당첨(\W|$)",
        "(\W|^)수익률(\W|$)",
        "(\W|^)추천주(\W|$)",
        "(\W|^)타점(\W|$)",
        "(\W|^)번개장터(\W|$)",
        "(\W|^)성인(용품)?(\W|$)",
        "(\W|^)토토(\W|$)",
        "(\W|^)카지노(\W|$)",
        "(\W|^)사설(\W|$)",
        "(\W|^)대출(\W|$)",
        "(\W|^)급전(\W|$)",
        "(\W|^)부동산(\W|$)"
    ]
    
    # check if the message matches any spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return True
    
    # if none of the patterns match, it's not spam
    return False
