def is_spam(message):
    import re
    
    # Check for typical spam phrases, urls, and numbers in a message
    spam_phrases = ["새로운 정보방", "상장스타트업", "계열사합병", "슈퍼개미", "수익", "노하우"]
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    numbers = re.findall('\d+', message)

    # Count 'spammy' words in a message
    spam_count = sum([message.count(spam_word) for spam_word in spam_phrases])

    # If there are more than 1 spammy words, or more than 1 urls and more than 2 numbers, classify as spam
    if spam_count > 1 or (len(urls) > 1 and len(numbers) > 2):
        return True
    else:
        return False