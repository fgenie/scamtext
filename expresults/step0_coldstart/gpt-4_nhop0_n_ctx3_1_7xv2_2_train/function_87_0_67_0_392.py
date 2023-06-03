
import re

def is_spam(text):
    spam_indicators = [
        r'당첨|최[^ ]*급|일체[^ ]*비용|무료|비밀번호|국[^ ]*회[^ ]*의[^ ]*원[^ ]*기[^ ]*업[^ ]*세[^ ]*력|상한[^ ]*가[^ ]*달[^ ]*성|경제야 놀자 TV 이석훈|▼단체방 관망하기|다|.서.|선.|물.|선..취|전달받은 고급 정보|투자계획|하락장|매매 성과|전일 현황',
        r'https?:\/\/[^ ]*kakao[^ ]*\.[^ ]*\/[^ ]*',
        r'상승 확정|금전요구 일절 없습니다.|매수하셔도 단기간에 익절'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True
            
    return False
