
import re

def is_spam(message: str):
    spam_indicators = [
        r'\b목표달성기념\b',
        r'\b디젠스\b',
        r'https://me2.kr',
        r'\b입증\b',
        r'\b차별화\b',
        r'\b추천주\b',
        r'\b여의도사람들',
        r'\b종목상담\b',
        r'\b실력으로\b',
        r'\b체험반\b',
        r'\b일주일만\b',
        r'\b미래가 달라집니다\b',
        r'\b주종/시황/뉴스\b',
        r'\b비번:'
    ]

    message = message.lower()

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    return False
