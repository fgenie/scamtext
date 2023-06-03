def is_spam(message):
    import re
    
    # Define spam indicators
    spam_indicators = [
        r"\d{1,}배",
        r"(?i)(?=.*목표가)(?=.*상승)",
        r"(?i)(?=.*폭등)(?=.*확정)",
        r"(?i)(?=.*무료)(?=.*강의)",
        r"\d{1,}%",
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        r"(?i)안내",
        r"(?i)(마감|종목|기록)",
    ]

    # Check if any spam indicators are found in the message
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    # If none of the spam indicators are found, it's not spam
    return False