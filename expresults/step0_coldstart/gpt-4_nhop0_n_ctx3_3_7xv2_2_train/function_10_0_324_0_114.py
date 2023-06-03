def is_spam(message: str) -> bool:
    
    import re
    from collections import Counter

    # Calculate string length and number of digits to get percentage of digits in the message
    string_length = len(message)
    digits = sum(c.isdigit() for c in message)
    digit_percent = (digits / string_length) * 100

    # Check for presence of URL shorteners, special characters, and consecutive capital letters
    url_shorteners = re.findall(r'(https?://[\w.-]+)', message)
    special_chars = re.findall(r'[\!@#\$%\^&\*\(\)]', message)
    consecutive_caps = re.findall(r'([A-Z]{3,})', message)
    
    # Check for repetition of same character more than 3 times
    characters = Counter(message)
    repeated_chars = {k:v for k, v in characters.items() if v > 3}

    # Define spam thresholds
    digit_threshold = 18 
    special_char_threshold = 0.1 * string_length
    consecutive_caps_threshold = 3
    repeat_char_threshold = 3

    # Classify as spam if thresholds are exceeded
    if (digit_percent > digit_threshold) or (len(special_chars) > special_char_threshold) or (len(consecutive_caps) > consecutive_caps_threshold) or (len(repeated_chars) > repeat_char_threshold):
        return True
    else:
        return False