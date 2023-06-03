def is_spam(message: str) -> bool:
    import re

    # Check for common spam elements: urls, numbers, special characters, and unusual spacing
    contains_url = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    contains_number = re.search(r'\d', message)
    contains_special_char = re.search(r'[!@#$%^&()*+=<>?,/-]', message)
    unusual_spacing = re.search(r'\w\s\s+\w|\w\s{3,}\w', message)

    # Calculate the number of criteria met
    spam_criteria = [contains_url, contains_number, contains_special_char, unusual_spacing]
    match_count = sum(1 for criterion in spam_criteria if criterion)

    # If at least three criteria are met, classify the message as spam
    return match_count >= 3