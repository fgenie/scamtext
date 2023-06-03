def is_spam(message: str) -> bool:
    import re

    # Define spam characteristics
    spam_keywords = ['증권사', 'F상장기업', '국내식약처', '루멘스', '미FDA승인', '신약개발관련주', '매10%', '매주BBQ',
                     '선물매매', '하루4번', '정부 300조지원', '검증된 수익률', '종목상담/추천', '여의도사람들4월체험반']
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\[\\],]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Check if message contains spam keywords or web URLs
    if any(keyword in message for keyword in spam_keywords) or re.search(url_regex, message):
        return True
    return False