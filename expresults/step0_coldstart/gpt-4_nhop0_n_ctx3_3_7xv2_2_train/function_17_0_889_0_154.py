
import re

def is_spam(text):
    # Check for the presence of URLs
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_regex, text)
    if len(urls) > 0:
        return True

    # Check for the presence of uncommon punctuation or symbols
    uncommon_symbols = ['>', '=']
    for symbol in uncommon_symbols:
        if symbol in text:
            return True

    # Check for the presence of unusual capitalization or whitespace patterns
    if re.search(r'[A-Z]{2,}', text) or re.search(r'\s{2,}', text):
        return True

    # Check for specific phrases or patterns associated with spam
    spam_phrases = ['상한가', '발표시', '추천주', '돌파', '단독제휴협약', 'AI사업본격화']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # If none of the above conditions are met, consider the message as normal
    return False
