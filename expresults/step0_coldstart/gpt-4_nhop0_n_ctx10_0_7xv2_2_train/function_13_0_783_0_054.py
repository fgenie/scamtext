
import re

def is_spam(message):
    # Define keywords, phrases and patterns usually found in spam messages
    spam_keywords = ['광고', '무료거부', '코드:', '톡', '부업실현', '수익', '상한가', '추천주', '최고의', '성공했어요']
    spam_phrases = ['월 천 고정수입', '매일15%', '추천 디젠스 벌써', '추천하시지 않을 고급정보', '성과를 안겨드리겠습니다']
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    
    # Check if any of the spam keywords or phrases are in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
            
    # Check if the message contains URLs
    if url_pattern.search(message):
        return True
    
    return False
