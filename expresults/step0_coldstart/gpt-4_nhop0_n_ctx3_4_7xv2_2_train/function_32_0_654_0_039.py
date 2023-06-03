def is_spam(text):
    import re

    spam_keywords = [
        "원한장", "만원", "십만원", "구경해보세요", 
        "카카오톡제재", "악성광고", "텔레그램", "기존 정보",
        "혜택 동일유지", "월마지막안내", "월마지막반"
    ]
    
    # Check for presence of spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True
            
    # Check for URLs in text
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(text):
        return True

    return False