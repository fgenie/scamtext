
import re

def is_spam(message):
    # Check for spam keywords in the message
    spam_keywords = ['해재투자동호회', '특별혜택', 'VIP', '체험반', '악성광고', '무료입장']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for multiple URL patterns in the message
    urls = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", message)
    if len(urls) >= 2:
        return True

    # Check for specific patterns used in some spam messages
    message_patterns = [
        r"습니다\. *이벤트",   # event within a single sentence
        r"발송 *비용",        # free of charge
        r"서울경제팍TV",      # Local TV
        r"▼ 클릭",          # buttons
        r"▲ 클릭",          # buttons
        r"\*[도]*\[애]*(광고)",        # disclaimers
        r"\[힌트\]",         # hints in brackets
        r"수.익",            # obfuscated text
        r"누적수익률",        # focused on returns 
    ]

    for pattern in message_patterns:
        if re.search(pattern, message):
            return True

    return False
