
import re

def is_spam(message):
    # Define spam patterns
    pattern1 = re.compile(r'\d+원[^\n]*[\d\-]+')
    pattern2 = re.compile(r'(https?[^\s]+)')
    pattern3 = re.compile(r'(上|산|쇼|체험|추천|보상)')

    # Check if any pattern appears in the message
    if re.search(pattern1, message) or re.search(pattern2, message) or re.search(pattern3, message):
        return True
    else:
        return False
