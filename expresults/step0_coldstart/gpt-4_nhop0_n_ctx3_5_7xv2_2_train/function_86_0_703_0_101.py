def is_spam(text):

    import re

    def check_keywords(content):
        spam_list = ['신청', '목표달성', '추천']
        for keyword in spam_list:
            if keyword in content:
                return True
        return False

    def check_url(content):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        if len(urls) > 0:
            return True
        return False

    def check_unusual_characters(content):
        unusual_characters = re.sub('[가-힣a-zA-Z0-9\\s]', '', content)
        if len(unusual_characters) > len(content) / 3:
            return True
        return False

    if check_keywords(text) or check_url(text) or check_unusual_characters(text):
        return True
    else:
        return False