
import re

def is_spam(message: str) -> bool:
    spam_indicators = [
        r"https?:\/\/*.+\.kr\/\w+",
        r"\d{1,2}[월일].+\d{1,2}[월일].*(체험반|종목|수익)",
        r".*(파이널|시작|여의도|클릭|선별).*(단독|체험반|종목|타자)"
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
            
    return False
