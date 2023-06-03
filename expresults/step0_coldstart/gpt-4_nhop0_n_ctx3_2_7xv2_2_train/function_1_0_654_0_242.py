
import re

def is_spam(message):
    keywords = ['무료', '체험', '발표', '상한가', '확정', '단독', '정보', '랭킹', '핵심', '상품', '선착순', '판매']
    
    # Check for excessive use of special characters
    special_char_count = sum([c in '!#$%&*+=?^_@' for c in message])
    if special_char_count / len(message) > 0.05:
        return True
    
    # Check for links using shortening services
    short_link_pattern = r'(https?://)?(bit\.ly/|goo\.gl/|me2\.kr/)'
    if re.search(short_link_pattern, message):
        return True
    
    # Count of the spam related keywords
    spam_keyword_count = sum([keyword in message for keyword in keywords])
    if spam_keyword_count > 1:
        return True

    # Check for excessive use of Korean characters
    korean_char_count = sum([c in '가각간갇갈감갑값갓갔강개객걀거걈걉거걊거걋거걌거걍거걎걏걐걑걓걔걕걖걘걜걤걧걫거걱거건걷검겁것게겐겜겠' for c in message])
    if korean_char_count / len(message) > 0.3:
        return True
    
    return False
