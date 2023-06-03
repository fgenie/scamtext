
import re

def is_spam(message):
    spam_keywords = ["만들기", "투자", "성공", "발표", "엠바고", "국내식약처", "정식허가", "미리입장", "미리확인", "긴급입수정보", "상한가", "AI로봇사업", "상장스타트업", "계열사합병", "기업명↓", "무료체험", "핵심정보"]
    normal_keywords = ["안녕하세요", "일양택배", "물품", "연락부탁드립니다", "내일", "다음에 보자", "문자 확인", "물품", "처리"]
    
    message = message.lower()
    url_pattern = re.compile(r'https?://[^\s]+')

    if url_pattern.search(message):
        for spam_keyword in spam_keywords:
            if spam_keyword in message:
                return True
        return False

    for normal_keyword in normal_keywords:
        if normal_keyword in message:
            return False

    return True
