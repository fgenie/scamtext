
import re

def is_spam(message):
    spam_keywords = [
        '추천주', '수익', '상한가', '환장', 'VVIP', '유료', '증권', '혜택', '지원금', '관망', '매수', '매도', '투자', '거래', '성과',
        '매매', '추천', '종목', '체험반', '광고', '상승', '상향', '하락', '단기', '장기', '카카오톡 제재', '안전한 업', '생활비 수익', '%',
        ' 백분율', '계약', '월 수익', '주식', '분석', '프로 성과', '다음 일정'
    ]
    
    message = message.lower()
    num_keywords = 0
    for keyword in spam_keywords:
        if keyword.lower() in message:
            num_keywords += 1
            
    num_urls = len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message))
    num_phonenumbers = len(re.findall('\\d{2,4}-?\\d{2,4}-?\\d{4}', message))

    if num_keywords > 1 or num_urls > 0 or num_phonenumbers > 1:
        return True
    return False
