import re

def is_spam(message):
    # Define patterns for spam messages
    url_pattern = r"(https?|ftp)://[^\s/$.?#].[^\s]*|www\.[^\s]*|[^\s]*\.(co|com|net|org|biz|info|kr)"
    money_pattern = r"([+-])(\s)*[\d,]+(\s)*[원$]"
    percentage_pattern = r"\d+(\s)*%"
    kaokaotalk_pattern = r"kakaosa.[co.]?kr"
    specific_word_pattern = r"(추천|더블림|분석).*"
    advertisement_pattern = r"(광고)"
    
    # Check if any pattern matches with the message
    if re.search(url_pattern, message) or re.search(money_pattern, message) or \
       re.search(percentage_pattern, message) or re.search(kaokaotalk_pattern, message) or \
       re.search(specific_word_pattern, message) or re.search(advertisement_pattern, message):
        return True
    else:
        return False