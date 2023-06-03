
import re

def is_spam(text):
    """
    Determines if the given text is a spam message or not.
  
    Args:
    text (str): The text string to be classified as spam or not spam.
  
    Returns:
    bool: True if the text is spam, and False otherwise.
    """
    # Check if the message contains keywords typically found in spam messages
    spam_keywords = ['추천', '종목', '▲', '공개', '확인', '지금', '가능', '판매', '광고', '무료', '거부', '벌거숭이', '끝물이']

    for keyword in spam_keywords:
        if keyword in text:
            return True
            
    # Check if the message contains a shortened URL or suspicious websites
    shortened_urls_pattern = r'(https?://[^\s]*[\w\.]*?me2[\w\-]*\.[^\s]*|https?://[\w\-]*bit\.ly[^\s]*|https?://[\w\-]*buly\.kr[^\s]*|https?://[\w\-]*tinyurl\.com[^\s]*|https?://[\w\-]*is\.gd[^\s]*|https?://[\w\-]*ow\.ly[^\s]*|https?://[\w\-]*tiny\.cc[^\s]*)'
    suspicious_websites_pattern = r'(https?://[^\s]*[\w\.]*?shinhan[\w\-]*\.[^\s]*|https?://[^\s]*[\w\.]*?신한은행[\w\-]*\.[^\s]*)'
    
    if (re.search(shortened_urls_pattern, text) or 
        re.search(suspicious_websites_pattern, text)):
        return True

    return False
