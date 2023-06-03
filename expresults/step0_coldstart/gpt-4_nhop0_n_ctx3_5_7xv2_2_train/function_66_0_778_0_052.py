
import re

def is_spam(message):
    keywords = ["VIP", "무료", "소니드", "적중", "체험반", "참여", "FROG"]
    has_keywords = any(keyword in message for keyword in keywords)
    
    percentage_of_capital_letters = sum(1 for char in message if char.isupper()) / len(message)
    high_percentage_of_capital_letters = percentage_of_capital_letters > 0.2
    
    number_of_urls = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message))
    
    return has_keywords or high_percentage_of_capital_letters or (number_of_urls > 0)
