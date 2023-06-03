
import re

def is_spam(message):
    spam_patterns = [
        r'\d{1,2}월\d{1,2}일',
        r'\d{1,2}%↑',
        r'https?://[\w./]+',
        r'[\w.]+@[a-zA-Z0-9]+',
        r'실력으로 보여드립니다',
        r'무료거부\s*0?80',
        r'목표가(:\s*|\s+)[:digit:]+',
        r'상한가',
        r'\d{1,2}년 연혁',
        r'금.{0,2}칙',
        r'체험반',
        r'참여',
        r'상한가',
        r'비밀번호',
        r'\d{1,2}배 이상',
        r'\d{7,15}',
        r'me2\.kr',
        r'opcn\-kakao\.com',
        r'무료로 <<"2주일내에" >>',
        r'\s+\+\s*한정\s*',
        r'\%(?=\s*이상|↓)',
        r'\d{1,2}월\d{1,2}일',
        r'\d{1,4}%이상',
        r'상위\s*\d{1,4}\%',
        r'대충\s*\d{1,4}\%',
        r'\+상한가'
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    return False
