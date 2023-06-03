
import re

def is_spam(message):
    # Check for spam indicators
    spam_indicators = [
        r'(광고)',
        r'(무료거부)',
        r'\d{2,}[.]',
        r'https?://\S{5,}',
        r'유료',
        r'상한가',
        r'수익률',
        r'익절',
        r'기회',
        r'(종목추천)',
        r'(안내드립니다)',
        r'(입장)',
        r'(%%)',
        r'(목표가)',
        r'(정보(가)?공개)',
        r'(공개합니다)',
        r'(오픈합니다)',
        r'(클릭후)',
        r'(입장해주세요)',
        r'(입장하시고)',
        r'(빠르게 참여하세요)',
        r'(상한가확정)',
        r'(개인정보취급방침)',
        r'(전문가)',
        r'(경력)',
        r'(약속합니다)',
        r'(따랐습니다)',
        r'(포인트리)',
        r'(참가자)',
        r'(신박한)',
        r'(승률)',
        r'(수익률?)',
        r'(달성)',
        r'(\d{2,}[월|년])',
        r'(▲|▼)',
        r'(누적수익률)',
        r'(선발대)',
        r'(혜택(들)?)',
        r'(익히)',
        r'(매집)',
        r'(차트)',
        r'(설명회)',
        r'(호재)',
        r'(오프라인광고)',
        r'(여러분|고객님)',
    ]
    
    # Check if any spam indicator is present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True
    
    return False
