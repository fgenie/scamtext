def is_spam(message):
    import re
    
    spam_indicator_phrases = [
        '목표달성기념', '추천 디젠스', 'vvip체험반', '기회 잡으세요', '1일기준500만원OK', '당일기준380%OK'
    ]
    
    # Check if message contains any spam_indicator_phrases.
    for phrase in spam_indicator_phrases:
        if phrase in message:
            return True

    # Check for suspicious URLs 
    if re.search(r'https?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message):
        url_count = len(re.findall(r'https?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message))
        shortened_urls = ['me2.kr', 'han.gl']
        for shortened_url in shortened_urls:
            if shortened_url in message:
                return True

    return False