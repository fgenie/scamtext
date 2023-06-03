
import re

def is_spam(message):

    # Identify spam patterns
    spam_patterns = [
        r'\b억(수|스)[자트]|\b체험(반|담|판)|\b(최소|최대)([0-9,])+%( 상승|하락)|\b[s]+\b(이래|한번|해보)서|\b(무료거부|무료 수신 거부)',
        r'https?://(han\.gl|bit\.ly|me2\.kr)/\w{2,}',
        r'\b(상한가|하한가)',
        r'\b꽃미(\.?)야',
        r'\b(외인|기관)에서 매집중인 종목',
        r'최(대|소)한 ([0-9,])+% 이(상|하)',
        r'\b(감사+합니다|다시한번|감사드립니+다|정말\?(감사+합니다|감사+합니다|감사+합니다|감사+합니다|감사+합니다))',
    ]
    
    # Check for spam patterns in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
