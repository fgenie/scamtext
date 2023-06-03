
import re

def is_spam(message):
    # Check for non-ascii characters and unusual combinations of letters and numbers
    non_ascii = re.search(r'[^\x00-\x7F]+', message)
    if non_ascii:
        return True
    
    # Check for multiple URLs or short URLs
    urls = re.findall(r'https?://\S+', message)
    if len(urls) > 1 or any(url.startswith('https://me2.kr/') or url.startswith('https://ko.gl/') or url.startswith('https://opcn-kakao.com/') or url.startswith('https://bit.ly/') for url in urls):
        return True
    
    # Check for overuse of special characters or capitalization
    if re.search(r'\W{4,}', message) or re.search(r'[A-Z]{4,}', message):
        return True
    
    # Check for common spam phrases
    spam_phrases = [
        '비밀 공시공개',
        '무료 참여 링크 클릭',
        '최소금요일',
        '목표가',
        '익 절 가',
        '누적수익률',
        '클릭 종목확인',
        'AI 자동 매매',
        '300~',
        '정보방에서 상세히 바로 공개됩니다',
        '전문가 경력'
    ]
    if any(phrase in message for phrase in spam_phrases):
        return True
    
    # If none of the above conditions are met, it is not spam
    return False
