
import re

def is_spam(message: str) -> bool:
    # Define spam-related patterns
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    number_pattern = r'\d'
    winning_pattern = r'당첨|적중|추천주|낙장|장미|전용|축하'
    advertisement_pattern = r'[광고]'
    unsubscribe_pattern = r'무료거부|무료 수신 거부'
    
    # Check for patterns in the message
    has_url = bool(re.search(url_pattern, message))
    has_number = bool(re.search(number_pattern, message))
    has_winning = bool(re.search(winning_pattern, message))
    has_advertisement = bool(re.search(advertisement_pattern, message))
    has_unsubscribe = bool(re.search(unsubscribe_pattern, message))

    # Classify the message as spam if at least two spam-related patterns are found
    spam_features_count = sum([has_url, has_number, has_winning, has_advertisement, has_unsubscribe])
    if spam_features_count >= 2:
        return True

    return False
