
import re

def is_spam(message: str) -> bool:
    # Regular expressions to match typical spam patterns
    spam_patterns = [
        r'(광고|\[광고\]).*하루\W?\d+,?\d+원', # Matches "광고" and some quantity of money
        r'(bit\.ly|me2\.kr|openkakao\.it)', # Matches typical short URLs
        r'(신규\W?\d+만원|추가이벤트|접수\W?[가-힣]{2,4}\W?\d+)',
        r'\d+%[\W]*[+]*입?금', # Matches percentage amounts for bonuses or promotions
        r'(무료거부|무료[0-9]{6,})', # Matches "무료거부" or starting with "무료" followed by several numbers
        r'(추천|경비|알에프|지아이텍|경동인베스트|상한가달성|하이딥|수익)',
        r'(말씀 드리겠습니다)', # Matches a phrase typically used in spam messages
        r'(목표달성기념, 추가종목)', # Matches a phrase about reaching goals
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return True

    return False
