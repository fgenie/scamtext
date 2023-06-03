def is_spam(text):
    import re

    spam_keywords = ["축하", "체험반", "클릭", "다음 타자", "주식", "추천", "5만원", "자동진행"]
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    contains_url = bool(url_pattern.search(text))
    has_spam_keyword = any(keyword in text for keyword in spam_keywords)

    return contains_url and has_spam_keyword