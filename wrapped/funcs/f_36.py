
import re

def is_spam(message):
    # Check for common spam phrases, words and symbols
    spam_phrases = [
        r'\b(무료|체험|vip|상승|성공|수익률|추천|주식|사람들|정보)\b',
        r'\b(회사|공시|종목|증권|반도체|제약|오후|분석|4월|3주차|최소)\b',
        r'\b(여의도|수익|멤버|직장인|투자|장기프로그램|마감)\b',
        r'\b(턴어라운드|매력적|인공지능|빅데이터|가상화폐|투기성|타점|분석)\b',
        r'\b(ur|https?|www.|http[\w=&#?,.:-]+|me2|opcn|a.to)\b',
        r'\b(_percent_|[_\-.]{2,})'
    ]
    
    # Combine spam phrases and words with 'or' clause
    spam_pattern = '|'.join(spam_phrases)

    # Check if the message matches the spam pattern
    if re.search(spam_pattern, message, re.IGNORECASE):
        return True
    else:
        return False
