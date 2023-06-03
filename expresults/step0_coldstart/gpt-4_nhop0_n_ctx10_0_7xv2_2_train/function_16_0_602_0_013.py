
import re

def is_spam(message:str )-> bool:
    # Check for excessive punctuation and capitalization
    punctuation_count = sum(1 for c in message if c in "!%")
    capital_count = sum(1 for c in message if c.isupper())
    if punctuation_count > 2 or capital_count > len(message) * 0.5:
        return True

    # Check for links and known spam-related domains
    links = re.findall(r'(https?://\S+)', message)
    spam_domains = {"me2.kr", "openkakao.at", "buly.kr", "openkakao.io", "nbet02.com"}
    for link in links:
        if any(spam_domain in link for spam_domain in spam_domains):
            return True

    # Check for keywords indicating potential spam
    spam_keywords = {"FDA", "지원", "수익", "알에프세미", "M반도체", "상담", "안전"}
    message_keywords = set(re.findall(r'\b\w+\b', message))
    if spam_keywords.intersection(message_keywords):
        return True

    return False
