
import re

def is_spam(text):
    
    spam_patterns = [
        # URL shorteners and patterns associated with scam websites
        r'(http|https)://(bit\.ly|me2\.kr|buly\.kr)[^\s]*',
        
        # Numbers and special characters repeated in sequence
        r'\d{2,}[%↑↓]',
        
        # Unusual amount of special characters (e.g. parentheses & brackets)
        r'[(){}<>]{3,}',
        
        # Unusual phrases commonly found in spam messages
        r'(슈퍼개미|선물|수익|감사합니다|카카오톡|모집|축하|교육|영업점|오픈초대|폭등|다음주도 이어서|상승)',
        
        # Repeated exclamation marks or question marks
        r'[!?]{2,}',
        
        # Words with an excessive amount of capital letters
        r'[A-Z\s]{4,}',
        
        # Pattern of time or percentage followed by an unusual word or character
        r'(\d[해선]%|\d+시(?:\s*간)?|\d+[\s-]*월)[^가-힣]+',

        # Repeated phrases or words
        r'(\b\w+\b)\W+\1'
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True

    return False
