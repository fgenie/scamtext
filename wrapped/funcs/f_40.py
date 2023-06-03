
import re

def is_spam(message):
    # URL patterns
    url_pattern1 = r'https?://[^\s]+'
    url_pattern2 = r'bit\.ly/[^\s]+'
    
    # Suspicious patterns
    spam_pattern1 = r'[0-9]{1,2}%?[-\s]?[\+↑]+'
    spam_pattern2 = r'상한가|익절가|추천주|무료체험|실현수익률'
    spam_pattern3 = r'\[[^\]]*클릭[^\]]*\]'
    
    # Combine all the patterns
    patterns = [url_pattern1, url_pattern2, spam_pattern1, spam_pattern2, spam_pattern3]
    combined_pattern = r'|'.join(patterns)
    
    # Check if any pattern is found in the message
    if re.search(combined_pattern, message):
        return True
    else:
        return False
