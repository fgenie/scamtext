def is_spam(message):
    import re

    # Checking for spam keywords and phrases
    spam_keywords = ["상한가", "무료", "성과", "대응", "협약", "발표", "급등", "공시", "클릭후", "kakaotalk", "me2.kr", "입장"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Checking for multiple links in the message
    link_pattern = r'(http|https|www\.)[^\s]+'
    links = re.findall(link_pattern, message)
    if len(links) > 1:
        return True

    return False