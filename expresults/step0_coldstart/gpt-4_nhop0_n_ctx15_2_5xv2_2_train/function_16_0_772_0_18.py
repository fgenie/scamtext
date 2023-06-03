
import re

def is_spam(text: str) -> bool:
    # Check for excessive use of special characters
    special_char_count = len(re.findall(r'[!@#$%^&*()_=+\[\]{}<>:;"''|\\,.?]', text))
    if special_char_count / len(text) > 0.1:
        return True

    # Check for presence of financial numbers and shortening of amounts
    if re.search(r'\d{1,3}(,|\.)\d{3}', text) or re.search(r'\d{1,3}(만원|천원)으로', text):
        return True

    # Check for presence of URLs containing suspicious domain names
    suspicious_domains = ["bit.ly", "me2.kr", "han.gl", "openkakao."]
    for domain in suspicious_domains:
        if domain in text.lower():
            return True

    # Check for excessive use of up arrow character
    up_arrow_count = text.count('↑')
    if up_arrow_count / len(text) > 0.05:
        return True
                
    return False
