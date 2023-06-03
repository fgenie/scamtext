
import re

def is_spam(message):
    # Patterns commonly found in spam messages
    spam_patterns = [
        r"\b클릭|종목확인|개장전|꼭 보십쇼|회사공시|목표가|익 절 가|예상 수익율",
        r"\b달성|상세히 바로 공개|최소 금요일|보름|주식어려운게 아닙니다",
        r"\b증권사 펀드매니저|실현수익률|수익률대회|애널리스트|누적수익률|전문가 경력",
        r"\b월 지속적|종목 적중|좋은결과|새로 만든 단타종목|자신 있습니다",
        r"https://opcn-kakao.com/",
        r"\b큰 도움이 될겁니다|조언 바탕으로 투자|유튜브 경제야 놀자 TV",
        r"\b투자 계획은|지속적인 하락장|등록 인증회사|종목수 프로",
        r"\b연이은 하락|진입 장벽|고민하지마세요",
        r"\b오픈카톡|전체 동료|투자 조언",
        r"\b공시보다 빠른 소식",
        r"\(광고\)|단체방 관망|금전요구 일절|무료거부|신년맞이 모집",
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return True
            
    return False
