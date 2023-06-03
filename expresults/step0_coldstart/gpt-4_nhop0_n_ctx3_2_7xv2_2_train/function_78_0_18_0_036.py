
import re

def is_spam(text):
    # Text preprocessing: Lowercase text and remove special characters
    text = re.sub(r'\W+', ' ', text.lower().strip())

    # Check for spam patterns
    spam_patterns = [
        r'\d+\s*\%',  # High percentage values
        r'특별|대형|본사|급세|새 가족분들|처음 방문 시|즉시 현금 지급|%|\$',  # Words associated with spam
        r'\w+[\.|@]\w+(\.\w+){1,2}|https?://\S+|bit.ly/\S+|me2.kr/\S+',  # URLs
        r'(광고)|(\[광고\])|{광고}',  # Advertisements
        r'배터리|무료수신거부|인증번호|톡\S+',  # Terms commonly used in spam messages
        r'\d+\+\d+'  # Numbers with '+' sign
    ]

    # Evaluate text against spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True

    return False
