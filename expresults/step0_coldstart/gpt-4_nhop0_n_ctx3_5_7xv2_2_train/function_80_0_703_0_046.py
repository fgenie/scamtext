
import re

def is_spam(message):
    # Check for common spam indicators
    ad_indicators = ['(광고)', '목표달성기념', '무료거부', '오늘\d+명마감', '→']
    url_regex = r'https?://\S+' 
    has_url = re.search(url_regex, message)

    # Compare message to ad_indicators
    for indicator in ad_indicators:
        if re.search(indicator, message):
            return True

    # Check if message contains a URL
    if has_url:
        return True

    # If none of the conditions above are met, classify message as normal
    return False
