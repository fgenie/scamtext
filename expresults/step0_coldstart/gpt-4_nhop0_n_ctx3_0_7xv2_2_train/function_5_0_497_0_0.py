
import re


def is_spam(message):
    # Check for urls
    make_money_urls = ["buly.kr", "me2.kr"]  # You can add more urls based on your knowledge
    url_patterns = re.compile(r'(https?:\/\/\S+)')
    urls = url_patterns.findall(message)

    for url in urls:
        for spam_url in make_money_urls:
            if spam_url in url:
                return True

    # Check for specific phrases or words
    spam_phrases = ['시작하루만에', '적중', '실력보셨죠?', '돈만내면']  # You can add more phrases or words based on your knowledge
    for phrase in spam_phrases:
        if phrase in message:
            return True

    return False
