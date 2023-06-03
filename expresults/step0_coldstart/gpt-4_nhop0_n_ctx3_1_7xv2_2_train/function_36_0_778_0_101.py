
import re

def is_spam(message: str) -> bool:
    # Searching for patterns typically observed in spam messages
    patterns = [
        r"https://\S+",  # URLs
        r"\d{1,2}일",    # Dates (e.g., 18일)
        r"\d{1,2}시",    # Times (e.g., 2시)
        r"\d{1,2}분",    # Minutes (e.g., 30분)
        r"\d{1,2}월",    # Months (e.g., 4월)
        r"\d{1,2}주차",  # Weeks (e.g., 3주차)
        r"▲|▼",         # Up/down arrows symbols
        r"[0-9,]+원",    # Currency (e.g., 100,000원)
        r"\d{1,2}\.\d{1,2}", # Percents (e.g., 0.3%)
        r"VIP|무료체험|정보방|입금번호|사은품", # Spam-related keywords
    ]

    for pattern in patterns:
        if re.search(pattern, message):
            return True

    return False
