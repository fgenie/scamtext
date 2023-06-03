
import re

def is_spam(text):
    # Pattern for non-alphanumeric characters
    non_alpha_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    # Pattern for suspicious URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\'(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Check if percentage of non-alphanumeric characters is too high
    non_alpha_count = len(re.findall(non_alpha_pattern, text))
    if non_alpha_count / len(text) >= 0.15:
        return True
    
    # Check for suspicious URLs
    if re.search(url_pattern, text):
        return True
    
    # Check for common spammer phrases
    spam_phrases = ['무료거부', '혜택', '광고', '제한', '급등주', '수익률']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    return False

