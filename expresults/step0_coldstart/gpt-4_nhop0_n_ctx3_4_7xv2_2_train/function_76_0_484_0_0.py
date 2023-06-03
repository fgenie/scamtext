
import re

def is_spam(message):
    # Check for URL shorteners
    url_shorteners = ['me2.kr']
    
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for certain words and phrases commonly found in spam messages
    spam_keywords = ['실력입증', '추천주', '돌파', '방금들어온정보', '체험VIP정보방', '안정적인수익',
                     '오후부터시작하는VIP체험반', '타점/분석', '여의도부장들의', '한농화성', '증권사부장출신']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    return False