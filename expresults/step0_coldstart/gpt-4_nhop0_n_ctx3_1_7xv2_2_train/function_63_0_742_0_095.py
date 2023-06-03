def is_spam(message: str) -> bool:
    import re

    # Check for suspicious keywords related to spam or promotions
    spam_keywords = ["VIP", "무료", "체험", "참여", "발표", "수혜주", "투자", "연상폭등"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URL shorteners, commonly used in spam messages
    url_shorteners_pattern = r"(https?:\/\/me2\.kr\/[\w]+)|(https?:\/\/bit\.ly\/[\w]+)"
    urls = re.findall(url_shorteners_pattern, message)

    if len(urls) > 0:
        return True

    # Check for unusually long messages, sometimes characteristic of spam
    if len(message) > 100:
        return True

    return False