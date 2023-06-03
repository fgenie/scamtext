
import re

def is_spam(message):
    spam_keywords = ["축하합니다", "당첨", "추천주", "시황", "분석", "수익률 100%", "대박 수익 종목", "유튜브 경제야 놀자 TV 이석훈",
                     "투자계획", "하락장", "지켜보신 후 아니다 싶으시면", "단체방 관망하기", "최근 3개월 매매 성과", "금전요구 일절 없습니다",
                     "두눈으로 똑똑히 보여드립니다", "직통 전화 번호", "관심주 확인", "단타 매매", "개인 비밀 번호", "특허 출원",
                     "아이디어 공모전", "무료 평생 등록", "하루 1시간", "꿀팁안내"]
    message = message.lower()
    
    for keyword in spam_keywords:
        if keyword.lower() in message:
            return True

    if re.search(r'https?://\S+', message):
        return True
    
    return False
