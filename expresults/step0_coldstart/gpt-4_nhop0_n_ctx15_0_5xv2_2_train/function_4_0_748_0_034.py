def is_spam(text):
    import re

    spam_keywords = ['무료', '광고', '추천', 'VIP', '수익', '첫충', '체험반', '무료거부', '최저', '상한가', '할인', '이벤트', '거래']

    # Check if the message contains spam keywords
    for keyword in spam_keywords:   
        if keyword in text:
            return True
    
    # Check if the message contains url shorteners or suspicious urls
    url_shorteners = ['bit.ly', 'me2.kr', 'buly.kr', 'dokdo.in', '특급주주정보', '신규통합방']
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    for url in urls:
        for shortener in url_shorteners:
            if shortener in url:
                return True
                
    return False