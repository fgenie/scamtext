
import re

def is_spam(content):
    spam_words = ['카지노', '긴급입수', '선물', '신규방', '악의적인', '파이낸스', '여의도', '최고급', '교수의', '세미+']
    url_regex = re.compile(r'https?://\S+|www\.\S+')
    excessive_punctuation = False
    word_threshold = 3

    detected_urls = url_regex.findall(content)
    if detected_urls:
        url_count = len(detected_urls)
        if url_count > 2:
            excessive_punctuation = True

    spam_word_count = 0
    for word in spam_words:
        if word in content:
            spam_word_count += 1

    if spam_word_count > word_threshold or excessive_punctuation:
        return True
    else:
        return False
