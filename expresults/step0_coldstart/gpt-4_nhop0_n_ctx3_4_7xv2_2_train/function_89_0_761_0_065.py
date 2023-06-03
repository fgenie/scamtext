
import re

def is_spam(text: str) -> bool:
    # Keywords commonly used in spam messages
    spam_keywords = ['당첨', '추천주', '시황', '분석', '수익률', '상장스타트업', '계열사합병', 'AI로봇사업',
                     '계열사합병', '광고', '코인', '전일통계', '수익', '축하합니다', '무료추천주', 'BTC폭스',
                     '참가하기', '성과표', '월요일부터 시작하는', '무료거부']
                     
    # Regular expression patterns to detect suspicious URLs in the text
    url_pattern = re.compile(r'(http[s]?://|www\.)\S+')

    # Count the number of spam keywords and suspicious URLs in the text
    spam_count = sum([text.count(keyword) for keyword in spam_keywords])
    url_count = len(url_pattern.findall(text))

    # If there are one or more spam keywords or suspicious URLs, classify the message as spam
    if spam_count > 0 or url_count > 0:
        return True

    # Otherwise, classify the message as normal
    return False
