
import re

def is_spam(text):
    # Check for common spam phrases
    spam_phrases = ['무료', '혜택', '추천', '상담']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for excessive use of special characters
    special_chars = '[@_!#$%^&*()<>?/\|}{~:]'
    special_count = sum([1 for c in text if c in special_chars])
    if special_count > 3:
        return True

    # Check for URL shorteners
    shorteners = ['bit.ly', 'me2.kr']
    for shortener in shorteners:
        if shortener in text:
            return True

    # Check for a pattern of a series of characters followed by numbers
    pattern = re.compile(r'[a-zA-Z]+\d+')
    matches = pattern.findall(text)
    if len(matches) > 1:
        return True

    return False
