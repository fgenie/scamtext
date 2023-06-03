def is_spam(message: str) -> bool:
    import re

    # List of spam keywords that can be found in spam messages
    spam_keywords = [
        r'\b추천\b', r'\b기념\b', r'\b종목\b', r'\b입니\b', r'\b온라인 게임\b', r'\b계열\b', r'\bVIP\b',
        r'\b에이전시\b', r'\b첫충\b', r'\b테.그램\b', r'\b무제한 충전\b', r'\b포인트\b', r'\b이벤트\b'
    ]

    # Clean the message by removing special characters and converting to lowercase
    cleaned_message = re.sub(r'[^\w\s]', '', message).lower()

    # Check if any of the spam keywords are found in the cleaned message
    for keyword in spam_keywords:
        if re.search(keyword, cleaned_message):
            return True

    return False