
import re

def is_spam(text: str) -> bool:
    # Remove whitespaces and lower the case
    text = text.replace(" ", "").lower()

    # Check for URL patterns and suspicious phrases
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(],|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    suspicious_phrases = ['두배', '가입', '종목', '매수', '체험반']

    # Check if the message contains URLs
    urls = re.findall(url_pattern, text)
    if len(urls) > 0:
        # Loop through each suspicious phrase
        for phrase in suspicious_phrases:
            # If the phrase is found in the text, it's a spam
            if phrase in text:
                return True

    # If no URL and suspicious phrase is found, it's not spam
    return False
