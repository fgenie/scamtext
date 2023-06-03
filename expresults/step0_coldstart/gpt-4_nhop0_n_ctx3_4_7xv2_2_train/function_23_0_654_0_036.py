
import re

def is_spam(text):
    spam_keywords = ["상장스타트업", "계열사합병", "투자반", "차별화", "시황", "무료체험"]
    spam_url_regex = re.compile(r'(http[s]?|me2\.kr)[:/#\?\.]+[-A-Za-z0-9_\.&/]*')

    text = text.replace(" ", "")
    if any(keyword in text for keyword in spam_keywords):
        return True
    if spam_url_regex.search(text):
        return True
        
    return False
