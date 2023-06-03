def is_spam(message):
    import re
    
    # Check for common spam keywords
    spam_keywords = ['무료입장', '유.료', '수.익', 'xx증권', '실현수익률', '힌트', '종목들', '안녕하세요', '클릭후', '발신', '1:1교육', '실현수.익']
    spam_keyword_count = sum([bool(re.search(keyword, message)) for keyword in spam_keywords])

    # Rule 1: More than 1 spam keyword present
    if spam_keyword_count > 1:
        return True

    # Rule 2: Multiple shortened URLs
    shortened_urls = ['me2.kr', 't.ly', 'bit.ly', 'tinyurl.com', 'ow.ly']
    shortened_url_count = sum([bool(re.search(url, message)) for url in shortened_urls])
    if shortened_url_count >= 2:
        return True

    # Rule 3: Unusual punctuation (광고, ※, ●)
    unusual_punctuation = ['광고', '※', '●']
    unusual_punctuation_count = sum([bool(re.search(punc, message)) for punc in unusual_punctuation])
    if unusual_punctuation_count > 0:
        return True

    # Rule 4: Multiple uppercase words
    uppercase_words = re.findall(r'\b[A-Z]{2,}\b', message)
    if len(uppercase_words) > 2:
        return True

    return False