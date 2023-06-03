
import re

def is_spam(message):
    # List of common spam words
    spam_words = ['현대 인수합병', 'AI로봇', '공개', '최종논의단계', '최소', '최대', '지금 폐',
                  '지금 냄새맡고', '유투브 진출 준비중', '핵심업체', '포항 2차전지', '엄청나게',
                  '외인/기관', '돈 안받습니다', '가입 없습니다', '각주 영업일 연속', '너무 오랜만이네요']

    # Check for spam words in the message
    for word in spam_words:
        if word in message:
            return True

    # Regular expression to match URLs
    url_regex = re.compile(r'https?://\S+')

    # If there are more than one URL in the message, classify it as spam
    if len(url_regex.findall(message)) > 1:
        return True

    return False
