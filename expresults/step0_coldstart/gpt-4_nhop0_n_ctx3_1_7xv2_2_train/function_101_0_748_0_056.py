
import re


def is_spam(message):
    # Define keywords associated with spam messages
    spam_keywords = ['무료상담', '추천드릴 종목', '카카오톡제재', '하루에 평균', '고급 정보', '상한가달성', '게시바', '진입시점제공']
    
    # Check if message contains any of the defined spam_keywords
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Define patterns associated with spam messages
    regex_patterns = [
        r"https?://\S+",                     # URLs
        r"\d{2,}\s*[.,]\s*\d{2,}",           # Any number with comma or dot separators
        r"◆\s*아래링크\s*클릭후\s*입장\s*◆",     # Sample keyword pattern
        r"bit\.ly/\S+",                      # Bit.ly URL shortener
        r"me2\.kr/\S+"                       # Another URL shortener
    ]

    # Check if message contains any patterns associated with spam messages
    for pattern in regex_patterns:
        if re.search(pattern, message):
            return True

    # If none of the spam indicators are found, return false
    return False
