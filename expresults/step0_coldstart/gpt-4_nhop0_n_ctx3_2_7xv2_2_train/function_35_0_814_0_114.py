def is_spam(text: str) -> bool:
    import re

    # Check for typical spam keywords and phrases
    spam_keywords = ['추천', '안내', '공개', '입장', '상승', '확인', '매수', '올라갑니다', '익절', '강요']
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for existence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.findall(text):
        return True

    # Check for mention of stocks or company codes
    company_code_pattern = re.compile(r'\([0-9]{6}\)')
    if company_code_pattern.findall(text):
        return True

    # Check for excessive use of special characters
    special_chars = ['+', '*', '%', '$', '#']
    special_chars_count = sum([text.count(char) for char in special_chars])
    if special_chars_count > 3:
        return True

    return False