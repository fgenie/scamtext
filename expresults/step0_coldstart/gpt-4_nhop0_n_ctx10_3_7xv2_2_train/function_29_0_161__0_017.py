
import re


def is_spam(text):
    keywords = ['매집', '비밀 종목', '수익', '체험반', '단타매매', '종목명', '상한가', '자동매매', '추천주', '분석', '수익률']
    spam_word_count = sum([1 for keyword in keywords if keyword in text])
    
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_count = len(re.findall(url_pattern, text))

    max_url_count = 1
    max_spam_word_count = 1

    return (url_count > max_url_count) or (spam_word_count > max_spam_word_count)
