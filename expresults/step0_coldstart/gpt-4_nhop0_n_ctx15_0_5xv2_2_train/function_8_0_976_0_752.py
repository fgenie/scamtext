
import re


def is_spam(message):
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for presence of numbers followed with 퍼센트 or % sign
    if re.search(r'\d+(\s*)[%퍼센트]', message):
        return True

    # Check for consecutive special characters
    if re.search(r'[-=`~!@#$%^&*()+\[\]{};\'"<>?/]', message):
        return True

    # Check for presence of 광고 or 문자 inside brackets
    if re.search(r'\(.*[광고|문자].*\)', message):
        return True

    # Check for 초대코드 or 비밀번호
    if re.search(r'[초대코드|비밀번호]', message):
        return True

    # Check for 수익률, 이익, 배당
    if re.search(r'[수익률|이익|배당]', message):
        return True

    # Check for 축하, 당첨, 추천
    if re.search(r'[축하|당첨|추천]', message):
        return True

    # Check for presence of 연락
    if re.search(r'[연락]', message):
        return True

    # Check if 송장번호 is present
    if re.search(r'[송장번호]', message):
        return True

    # Check for 주식 or 상한가
    if re.search(r'[주식|상한가]', message):
        return True

    # Check for 한 or 주차 in the message
    if re.search(r'[한|주차]', message):
        return True

    # Check for presence of 적중
    if re.search(r'[적중]', message):
        return True
        
    return False
