
import re

def is_spam(message):
    # List of common spam words or phrases
    spam_keywords = ["반찬정보", "백조", "전달받은", "대기하시면 종목 오픈", "https://han.gl/", "3일만 관망해", "급상승", "신뢰", "종목", "버스회사", "정보이므로", "최소 150%", "믿고거래하는곳", "10대여성복", "추천드릴", "진료 후 만족도", "티커1티커2티커3", "완판", "감명", "체험반", "VFIP"]
    # List of common normal words or phrases
    normal_keywords = ["안녕하세요", "오늘", "모임", "지내시죠", "연락", "다시", "궁금하신거", "넵", "좀 있다 보자고", "실력보셨죠", "진료시간 안내", "구입하고 싶은데"]

    # Check for presence of spam words
    for spam_keyword in spam_keywords:
        if spam_keyword in message:
            return True

    # Check for presence of normal words
    for normal_keyword in normal_keywords:
        if normal_keyword in message:
            return False

    # Check for URLs in message
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    if len(urls) > 0:
        return True

    return False
