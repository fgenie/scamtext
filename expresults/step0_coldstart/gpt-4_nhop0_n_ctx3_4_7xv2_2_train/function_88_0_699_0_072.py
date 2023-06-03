import re

def is_spam(message):
    # Look for spam indicators in the message
    spam_indicators = [
        r'https?://', # presence of URLs
        r'\d{1,2}주', # presence of time period in weeks
        r'\d{1,2}월', # presence of time period in months
        r'부업', # Side Job
        r'육아맘', # Parenting
        r'가입', # Subscription
        r'추천주 현황', # stock recommendation status
        r'[가-힣]{3}박했습니다', # Word ending with 박했습니다 (indicating ongoing activity)
    ]

    # If any of the spam indicators are present in the message, return True
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    # If none of the spam indicators are present, return False
    return False