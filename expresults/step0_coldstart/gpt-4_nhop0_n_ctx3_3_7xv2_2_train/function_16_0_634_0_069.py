def is_spam(message):
    import re

    # Check for common spam phrases
    spam_phrases = ["목표달성기념", "추천", "디젠스", "할인", "고객님께서 요청하신", "해외선물", "VIP정보방", "빠른입장"]
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for shortened URLs
    if re.search(r'http[s]?://\w{1,3}\.', message):
        return True

    # Check for excessive use of special characters
    non_alphanumeric_count = sum([1 for c in message if not (c.isalnum() or c.isspace())])
    if non_alphanumeric_count > len(message) * 0.3:
        return True

    return False