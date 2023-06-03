
import re

def is_spam(message):
    """
    This function determines if the given message is spam or not.
    Args:
    message (str): The message to be classified as spam or not.

    Returns:
    bool: True if the message is spam, False otherwise.
    """

    # Patterns to find in the message
    url_pattern = r'(http|https)://[^\s]*'
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    phone_pattern = r'(\+?\d{1,2})?\d{10,11}'

    # Check for urls, emails, and phone numbers in the message
    if re.search(url_pattern, message) or re.search(email_pattern, message) or re.search(phone_pattern, message):
        return True

    # Check for common spam words and phrases
    spam_keywords = [
        '지원받고', '적중','수익','체험반', '입장코드', '통화량',
        '광고', '최고급 정보', '가상의 장벽', '유튜브 공식',
        '전달받은', '특별 공개', '초대', '팔로우+',
        '페이스북 이벤트', '단체방', '제한 인원', '광고 전화', '중요한 공지',
        '추천', '무료로 받아', '동향 전망', '등락', '강세',
        '프로모션', '공식 인증', '도박', '파워 볼']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    return False
