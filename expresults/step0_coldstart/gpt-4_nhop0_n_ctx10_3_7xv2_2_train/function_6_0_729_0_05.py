
import re

def is_spam(text):
    # Check for common spam indicators
    spam_indicators = [
        r"\b광고\b",
        r"\b추천\b",
        r"https?:\/\/[^\s]+",
        r"\b성공\b",
        r"\b수익\b",
        r"\b투자\b",
        r"\b확인\b",
        r"\b지긋지긋한\b",
        r"\b지원\b",
        r"\b지급\b",
        r"\b초대합니다\b",
        r"\b소액투자\b",
        r"\b가난한\b",
        r"\b동학개미\b",
        r"\b개미 인생\b",
        r"\b루멘스\b",
        r"\b나스닥\b",
        r"\b체험반\b"
    ]

    # Check for presence of spam indicators in the text
    for spam_indicator in spam_indicators:
        if re.search(spam_indicator, text):
            return True
        
    # If no spam indicators are found, return False
    return False
