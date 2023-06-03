
import re

def is_spam(text):
    spam_keywords = ["추천", "공개", "수익률", "익 절 가", "목표가", "펀드매니저", "주식 수익률", "전문 애널리스트", "누적수익률"]

    if len(text) > 50 and any(keyword in text for keyword in spam_keywords):
        return True
    
    url_pattern = re.compile('https?:\/\/[\w\-.]+\/[\w\-=]+')
    urls = url_pattern.findall(text)
    
    if urls:
        url_count = len(urls)
        short_url_pattern = re.compile('(?:https?:\/\/)?(?:bit\.ly|me2\.kr|opcn\-kakao\.com)\/[\w\-=]+')
        short_url_count = len(short_url_pattern.findall(text))
        if url_count >= 2 and short_url_count / url_count >= 0.5:
            return True

    return False
