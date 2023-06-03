def is_spam(message):
    import re
    
    spam_keywords = ['광고', '무료수신거부', '개장전', '체험반', '비용 없습니다', '오후 2시', '실. 제. 성. 과', '지원금', '아이디', '하루1시간', '무료거부', '스닥닷컴',
                     'HTS/MTS', '골드해선그룹', '수수료', '기준', '최대수혜주', '타업체', '방 종료되었습니다', '신규방 안내', '상승할 종목', '수익률']
    spam_url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    excessive_symbols = re.compile(r"[!$()_%?*,-/']{2,}")

    if any(keyword in message for keyword in spam_keywords) or re.findall(spam_url_pattern, message) or excessive_symbols.search(message):
        return True

    return False