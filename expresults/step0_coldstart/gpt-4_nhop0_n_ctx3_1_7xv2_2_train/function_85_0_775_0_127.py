
import re
import string

def is_spam(text):
    # Check for presence of URLs in message
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_match = url_pattern.search(text)
    
    # Check for presence of special characters
    special_chars = "@#※%<>;"
    special_chars_match = any(char in special_chars for char in text)
    
    # Check for repetition of words (consecutive or non-consecutive), more than 3 times
    words = text.lower().split()
    repitition_count = {word: words.count(word) for word in words}
    repeated_words = [word for word, count in repitition_count.items() if count > 2]
    
    # Check for excessive use of punctuation marks
    punctuations = set(string.punctuation)
    excessive_punctuation = sum(1 for char in text if char in punctuations) > len(text) * 0.2
    
    return bool(url_match or special_chars_match or repeated_words or excessive_punctuation)
