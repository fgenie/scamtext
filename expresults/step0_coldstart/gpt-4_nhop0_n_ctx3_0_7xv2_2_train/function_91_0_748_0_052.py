def is_spam(text):
    import re
    from collections import Counter
    
    def has_url(text):
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
        if len(urls) > 0:
            return True
        else:
            return False

    def has_korean_words(text):
        korean_words = re.findall('[가-힣]+', text)
        if len(korean_words) >= 6:
            return 1
        return 0

    def consecutive_uppercase_percentage(text):
        uppercase_groups = re.findall('[A-Z]+', text)
        group_lengths = [len(group) for group in uppercase_groups]
        total_uppercase_letters = sum(group_lengths)
        percentage = (total_uppercase_letters * 100) // len(text)
        return percentage

    def has_korean_url_shortener(text):
        return bool(re.search(r'me2\.kr', text))
    
    features = {
        'has_url': has_url(text),
        'has_korean_words': has_korean_words(text),
        'uppercase_letters_percentage': consecutive_uppercase_percentage(text),
        'has_korean_url_shortener': has_korean_url_shortener(text)
    }

    weights = {
        'has_url': 2.0,
        'has_korean_words': 2.0,
        'uppercase_letters_percentage': 3.0,
        'has_korean_url_shortener': 5.0
    }

    score = sum([weights[feature] * int(features[feature]) for feature in features])
    return score >= 6