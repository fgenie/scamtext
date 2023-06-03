import re

def is_spam(message):
    # Check for spam indicators
    spam_indicators = [
        r'\b광고\b',
        r'\b평균 수익.*대공개',
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'\b무료거부',
        r'\b오픈카톡',
        r'\b최대.*할인',
        r'\b카톡방 입장',
        r'\b공시 종목',
        r'\b% 이상 상승',
        r'\b거래량[0-9]*배']

    # Check if any spam indicator is present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    # If no spam indicator is present, classify the message as normal
    return False