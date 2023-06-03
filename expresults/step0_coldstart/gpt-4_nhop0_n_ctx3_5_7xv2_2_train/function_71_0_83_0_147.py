
import re

def is_spam(message):
    # Check for common spam features in the message.
    message = message.lower()
    
    # Feature 1: Presence of bit.ly or other short URLs
    short_url_pattern = r'bit\.ly|goo.gl'
    if re.search(short_url_pattern, message):
        return True
    
    # Feature 2: Presence of special characters and percentage signs
    special_char_pattern = r'[★※%@％\(\)]'
    if re.search(special_char_pattern, message):
        return True

    # Feature 3: Presence of 매일, 처음, 무료 and 체험 words, common in Korean spam messages
    spam_indicator_words = r'매일|처음|무료|체험'
    if re.search(spam_indicator_words, message):
        return True
    
    # Feature 4: Inclusion of consecutive spaces, common in spam messages
    consecutive_spaces = r'\s{2,}'
    if re.search(consecutive_spaces, message):
        return True

    # If none of the features are found, it's probably not a spam message
    return False
