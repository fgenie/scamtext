
import re

def is_spam(message: str) -> bool:
    # Checking if the message contains a URL pattern
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    url_matches = url_pattern.findall(message)

    # Checking for spam keyword patterns
    spam_pattern = re.compile(r'일만원으로|천만원만들기|배워보기|투자|성공|최소인원|부자되기프로젝트|카톡방|실력보셨죠|종목')
    spam_matches = spam_pattern.findall(message)

    # If the ratio of numbers to characters higher than a certain threshold or the message has spam keywords and a URL, classify it as spam
    numbers = sum(c.isdigit() for c in message)
    chars = sum(c.isalpha() for c in message)
    ratio = numbers / (chars + 1)  # adding 1 to avoid division by zero
    if (ratio > 0.3 and url_matches) or (spam_matches and url_matches):
        return True
    return False
