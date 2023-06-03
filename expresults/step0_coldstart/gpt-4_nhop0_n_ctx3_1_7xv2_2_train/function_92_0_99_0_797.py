
import re
from urllib.parse import urlparse

def is_spam(message):
    # Check for excessive use of special characters to avoid filtering
    if re.search(r"[^a-zA-Z0-9\s]{3,}", message):
        return True

    # Check for suspicious phrases often found in spam messages
    spam_phrases = [
        "상승", "매주", "무료거부", "증 권", "최고급", "비용",
        "공시발표", "상한가달성", "입장", "익절", "단어"
    ]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for excessive use of URLs
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
    if len(urls) > 1:
        return True

    # Check for suspicious domains in URLs
    spam_domains = ["me2.kr", "openkakao.it"]
    for url in urls:
        domain = urlparse(url).netloc
        if domain in spam_domains:
            return True

    # If none of the above patterns are found, the message is likely not spam
    return False
