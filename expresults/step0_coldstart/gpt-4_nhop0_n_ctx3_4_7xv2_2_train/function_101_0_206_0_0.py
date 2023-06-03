
import re

def is_spam(message): 
    # Searching for spam elements and indicators
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    percentages = re.findall(r'\d+%?[\u2191]', message)
    symbols = re.findall('(\$[\w.]|-[\w.]|(?:\\d+,)*\\d+(?:\\.\\d{1,2})?%?)|[+]', message)
    suspicious_keywords = ['마감', '상한가', '신규', '투자', '체결']
    
    spam_count = 0
    if len(urls) > 0:
        spam_count += 1
    if len(percentages) > 0:
        spam_count += 1
    if len(symbols) > 1:
        spam_count += 1
    if any(keyword in message for keyword in suspicious_keywords):
        spam_count += 1

    # If there are multiple spam elements, classify as spam
    if spam_count > 2:
        return True
    
    return False
