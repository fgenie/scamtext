
import re

def is_spam(text):
    # Convert the text to lowercase for easier processing.
    text = text.lower()

    # Check for spam indicators like "축하드립니다", "클릭후 무료입장", "장소: 이마트 성수점 본사 6층 대당강 행사장"
    # etc. and return True if any of these phrases are present. Also check for shortened URLs.
    spam_indicators = [
        r"축하드립니다",
        r"클릭후 무료입장",
        r"장소: 이마트 성수점 본사 6층 대당강 행사장",
        r"\bhttp[s]?://[^\s]*\.\w{2,4}/\w+\b"
    ]
    
    # Iterate through the spam indicators and check if they are present in the text.
    for indicator in spam_indicators:
        if re.search(indicator, text) is not None:
            return True

    # If none of the spam indicators are present, return False.
    return False
