
import re

def is_spam(text):
    spam_words = ['악성광고', '상한가', 'VIP', '체험방', '반값할인', '무료상담', '추천주', '상승주', '매집주', '최저가', '즉석지급', '텔레그램',
                  'bit.ly', 'https://me2.kr', '포인트지급']
    normal_words = ['안녕하세요', '근황', '생일 축하', '지금 어디', '뭐하고 있어', '입금']
    
    text = text.lower()
    spam_count = 0
    normal_count = 0

    # Checking for spam words
    for word in spam_words:
        if word.lower() in text:
            spam_count += 1
            
    # Checking for normal words
    for word in normal_words:
        if word.lower() in text:
            normal_count += 1
            
    # If there are more spam words than normal words, classify as spam
    if spam_count > normal_count:
        return True
    else:
        return False
