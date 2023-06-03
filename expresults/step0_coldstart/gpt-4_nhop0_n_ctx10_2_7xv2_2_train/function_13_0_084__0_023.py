def is_spam(message: str) -> bool:
    import re

    # Initialize spam indicators
    spam_indicators = [
        r'\d{1,2}\\.\\d{1,2}%',
        r'\+[0-9]+'+'%', 
        r'https?:\\/\\/[a-zA-Z0-9]+\\.[a-zA-Z]+\\/[a-zA-Z0-9]+',
        r'▼',
        r'(염|김|이)[a-zA-Z0-9가-힣]*',
        r'원 마감',
    ]

    # Sum the spam indicators presence
    spam_indicators_sum = 0
    for indicator in spam_indicators:
        if re.search(indicator, message):
            spam_indicators_sum += 1

    # Check if the sum of spam indicators exceeds the threshold
    threshold = 2
    if spam_indicators_sum >= threshold:
        return True
    else:
        return False