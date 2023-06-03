
import re

def is_spam(text):
    spam_words = ['클릭', '링크', '성과', '상승', '상한가', '익절', '손실', '종목', '매수', '공시']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    openkakao_pattern = re.compile(r'openkakao\.[a-zA-Z]+/[a-zA-Z0-9]+')
    excessive_whitespace = re.compile(r'\s{2,}')
    
    contains_url = url_pattern.search(text) is not None or openkakao_pattern.search(text) is not None
    contains_excessive_whitespace = excessive_whitespace.search(text) is not None
    spam_word_count = sum([1 for word in spam_words if word in text])
    
    if contains_url and contains_excessive_whitespace and spam_word_count > 2:
        return True
    else:
        return False
