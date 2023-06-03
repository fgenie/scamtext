
import re

def is_spam(message):
    # Check for common spam keywords and patterns
    spam_keywords = ['무료', '축하', '발표', '입장', '엠바고']
    spam_pattern = re.compile('|'.join(spam_keywords), re.IGNORECASE)
    
    # Check for URL shortening services
    short_url_pattern = re.compile(r'(?:https?://(?:bit\.ly|me2\.kr|ani\..{2})/[\w/]+)', re.IGNORECASE)

    # Check for typical commercial advertisement phrases
    commercial_pattern = re.compile(
        r'(?:매일|선착|무료거부|클릭|다음 타자|번호:?|바로가기|최소3연상 파워)|웹하드|원할무|상품안내',
        re.IGNORECASE
    )

    if spam_pattern.search(message) or short_url_pattern.search(message) or commercial_pattern.search(message):
        return True
    else:
        return False
