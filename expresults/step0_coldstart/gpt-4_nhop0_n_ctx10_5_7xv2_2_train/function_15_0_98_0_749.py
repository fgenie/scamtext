
import re

def is_spam(message: str) -> bool:
    
    spam_patterns = [
        r'\b[\d\s\.-]+',
        r'(?:https?://)?(?:www\.)?me2\.kr',
        r'(?:https?://)?(?:www\.)?링크클릭후 \s* 입장',
        r'(?:https?://)?(?:www\.)?지금 \s* 입장',
        r'(?:https?://)?(?:www\.)?openkakao\.at',
        r'목표달성기념',
        r'반드시 확인해주세요',
        r'내일 개장전 체크하세요',
        r'(?:\*美FDA승인 임상)|정부 300조지원',
        r'해.외.선.물.',
        r'비밀번호 : \d{4}',
        r'K B 증 권',
        r'최고급 정보',
        r'딱 1주만 매수',
        r'"4월파이널VIP체험반"',
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
            
    return False
