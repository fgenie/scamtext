
import re

def is_spam(message):
    # Spam indicators
    keywords = ['VIP', 'FDA', '지원', '참여', '추천', '분석', '시황', '주소', '정부', '신약', '홈페이지']
    url_pattern = r"(https?://[^\s]+)"
    special_characters_ratio = 0.3

    # Check for presence of URLs
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        has_url = True
    else:
        has_url = False

    # Check for presence of keywords
    keywords_found = [keyword for keyword in keywords if keyword in message]
    has_keyword = len(keywords_found) > 0

    # Calculate ratio of special characters
    special_char_count = sum([1 for char in message if not char.isalnum()])
    special_char_ratio = special_char_count / len(message)

    return has_url or has_keyword or special_char_ratio >= special_characters_ratio
