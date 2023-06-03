def is_spam(message):
    import re

    # Check for common spammy words/phrases
    spam_words = ['무료수신거부', '특별전', '참여하기', '클릭후 입장']
    for word in spam_words:
        if word in message:
            return True

    # Check for suspicious URLs
    suspicious_urls = ['me2.kr', 'openkakao.it', 'vo.la', 'dokdo.in']
    for url in suspicious_urls:
        if url in message:
            return True

    # Check for high percentage gain claims
    regex_percentage = r'(\d{1,3})\s?[퍼센.\/%]\s?(\W{1,2})'
    result = re.search(regex_percentage, message)
    if result:
        gain = int(result.groups()[0])
        if gain > 20:
            return True

    # None of the spammy indicators were found, so it's probably a normal message
    return False