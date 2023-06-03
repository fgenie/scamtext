def is_spam(message):
    import re

    spam_keywords = [
        '광고', '추천', '무료', '일론머스크', '매일같이', '사주', '역학', '풍수', '챗 GPT', '알파고', '이세돌', '멘탈', '등록번호', '%', '알파고',
        '투자', '수익', '실현', '해외선물', '향↑', '축하', '차한잔', '승수', '상승', '기준' , '현금 증발', '방송 폭주', '5만원', '1억원',
        '구매', '추가', '지급', '선물'
    ]
    
    url_regex = r'https?:\/\/(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    
    spam_count = sum(keyword.lower() in message.lower() for keyword in spam_keywords)
    url_count = len(re.findall(url_regex, message))

    return spam_count > 0 or url_count >= 2