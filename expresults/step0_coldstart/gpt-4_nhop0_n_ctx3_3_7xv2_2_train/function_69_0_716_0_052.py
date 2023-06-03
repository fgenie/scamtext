
import re

def is_spam(text):
    # Check for keywords, urls, and percentages
    spam_keywords = ['무료', '수익', '부자', '노하우', '공개']
    url_pattern = r'(http|https)?:\/\/(\w+\.\w+)(\/\S*)?'
    percent_pattern = r'\d+%'

    # Count the number of spam keyword occurrences
    keyword_count = sum([1 for keyword in spam_keywords if keyword in text])

    # Check if text contains a URL or a percentage
    contains_url = re.search(url_pattern, text) is not None
    contains_percent = re.search(percent_pattern, text) is not None

    # Check if text starts with 광고
    starts_with_ad = text.startswith("(광고)")

    if keyword_count > 2 or contains_url or contains_percent or starts_with_ad:
        return True
    else:
        return False
