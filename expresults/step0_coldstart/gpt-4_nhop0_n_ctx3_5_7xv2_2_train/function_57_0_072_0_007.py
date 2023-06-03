
import re

def is_spam(text: str) -> bool:
    """
    A function to classify the given text as spam or not
    """
    spam_keywords = ['계신가요', '급등예정', '실현', '성.+순.+open', '종료']

    # Check for spam keywords in text
    for keyword in spam_keywords:
        if re.search(keyword, text):
            return True

    # Check for URL in the text
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    
    if len(urls) > 0:
        # Check for spammy URLs
        spam_urls = ['gg.gg', 'ko.gl']
        for url in urls:
            for spam_url in spam_urls:
                if spam_url in url:
                    return True
                    
    return False
