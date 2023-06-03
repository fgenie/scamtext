
import re

def is_spam(message):
    target_price = ['목표가:', '상승 보.장']
    increased_traffic = ['거래량', '매수세', '폭등']
    advertising = ['(광고)', '신청']
    urls = ['kakaotalk.at', 'https://', 'ko.gl']
    
    # Check for specific words and phrases commonly found in spam messages
    for spam_word in target_price + increased_traffic + advertising:
        if spam_word in message:
            return True

    # Check for URLs
    if any(url in message for url in urls):
        return True
    
    # Match and count phone numbers
    phone_regex = re.compile(r"\d{2,4}\d{3,4}\d{4}")
    phone_count = len(phone_regex.findall(message))
    
    if phone_count > 0:
        return True

    return False
