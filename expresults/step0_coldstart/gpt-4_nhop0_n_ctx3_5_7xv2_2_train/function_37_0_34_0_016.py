
import re

def is_spam(message):
    # Check for repeated URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 1:
        return True
    
    # Check for unusual capitalization patterns and message repetitions
    capitalization_pattern = re.compile(r'[A-Z]{2,}')
    caps = re.findall(capitalization_pattern, message)
    non_capitalized_words = sum(word.islower() for word in message.split())

    # Check for keywords indicating sales or promotion information
    spam_keywords = ["제휴", "파이널", "체험반", "상한가", "발표", "협약", "단독입수"]

    keyword_count = 0
    for keyword in spam_keywords:
        keyword_count += message.count(keyword)
    
    # Classify as spam if any of the spam keywords were found
    # and the capitalization pattern is unusual or message is repetitive
    if keyword_count > 0 and (len(caps) > 2 or non_capitalized_words < 3):
        return True
        
    # Classify as not spam otherwise
    return False
