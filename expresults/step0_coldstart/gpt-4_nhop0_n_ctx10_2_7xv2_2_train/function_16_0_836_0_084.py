def is_spam(message: str) -> bool:
    import re

    # Check if the message has the word "광고" or "코드" or "무료거부" or "▼" or "▲" or "http" or "https", which are common in spam messages.
    spam_keywords = ["광고", "코드", "무료거부", "▼", "▲", "http", "https"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check if the message contains a string like "원" or "%" followed by a number, which could indicate spammy promotions.
    price_or_percentage_pattern = re.compile(r'(\d+(\,(\d{3}))*(원|%))|(\d+(\.(\d{2}))*(원|%))')
    if re.search(price_or_percentage_pattern, message):
        return True

    # Check if the message contains a shortened link (e.g. me2.kr or han.gl)
    shortened_url_pattern = re.compile(r'\b(me2\.kr|han\.gl)\b')
    if re.search(shortened_url_pattern, message):
        return True

    # Check if the message is written using many Korean multiple question marks or exclamations
    multiple_punctuation_pattern = re.compile(r'[?!]{2,}')
    if re.search(multiple_punctuation_pattern, message):
        return True

    # If none of the above conditions are met, the message is considered normal.
    return False