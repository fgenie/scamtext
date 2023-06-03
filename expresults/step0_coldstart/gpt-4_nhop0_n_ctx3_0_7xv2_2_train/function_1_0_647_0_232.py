def is_spam(message):
    import re

    # Check if there is an excessive use of special characters or capital letters
    special_char_count = sum([1 for char in message if char in "!@#$%^&*()_+-=[]{};':\"|,<>.?/"])
    capital_letter_count = sum([1 for char in message if char.isupper()])
    total_length = len(message)
    special_char_ratio = special_char_count / total_length
    capital_letter_ratio = capital_letter_count / total_length

    if special_char_ratio > 0.1 or capital_letter_ratio > 0.5:
        return True

    # Check for phone numbers or email addresses
    phone_regex = re.compile(r'\d{2,4}[-\s.]?\d{2,4}[-\s.]?\d{2,4}')
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    if phone_regex.search(message) or email_regex.search(message):
        return True

    # Check for suspicious keywords or phrases
    spam_keywords = ['배.t팅', '적립금', '일.환', '적.금']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False