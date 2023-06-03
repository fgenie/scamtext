
import re

def is_spam(text: str) -> bool:
    # Search for phrases and patterns commonly found in spam messages
    spam_indicators = [
        r'(?:클|단독)[\w ]*[게|공시|선|특|투자|실한|매도].*(?:주|시작)',  # Korean phrases offering stock tips
        r'\d{2}[일|월][$\d]+?%',  # Algorithmically generated returns claims
        r'https?://(?!me2\.kr)[\w.\-_/]+',  # Suspicious URLs
    ]

    # If any indicator is present, it's spam
    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True

    # If no indicators are present, it's a normal message
    return False
