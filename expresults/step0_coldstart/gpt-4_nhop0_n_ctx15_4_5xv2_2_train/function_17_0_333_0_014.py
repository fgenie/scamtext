import re

def is_spam(text: str) -> bool:
    # Check for common spam phrases
    spam_phrases = [
        '광고', '지원금', '신청', '추천주', '수익률', '무료거부', '지급', '누적수익률', '코드',
        '원', '비용', '%', '더', '합병', '지금', '개미', '이벤트', '영업일',
    ]
    
    num_spam_phrases = sum(1 for phrase in spam_phrases if phrase in text)

    # Check for URLs
    url_pattern = re.compile(r'(http(s?):\/\/|www\.)\S+')
    urls = url_pattern.findall(text)
    text_without_urls = url_pattern.sub('', text)

    # Count digits in the text
    num_digits = len(re.findall(r'\d', text_without_urls))

    # Check for unusual structure of the text
    num_words_in_text_without_urls = len(text_without_urls.strip().split())
    num_words_in_text = len(text.strip().split())
    prop_words_removed_without_urls = (num_words_in_text - num_words_in_text_without_urls) / num_words_in_text

    return (
        num_spam_phrases >= 3 or
        num_digits >= 5 and len(urls) >= 1 or
        prop_words_removed_without_urls >= 0.5
    )