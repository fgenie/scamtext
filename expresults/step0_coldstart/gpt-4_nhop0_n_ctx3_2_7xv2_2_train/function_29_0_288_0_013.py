
import re

def is_spam(message):
    spam_keywords = ["만원", "십만원", "증권", "최고급", "비용", "이익", "상승", "매수", "공시", "폭등", "익절", "재료", "스윙",
                     "성과", "무료", "수익", "상한가", "주식", "테마주", "수급주", "반대로", "상승여력",
                     "주안으로","올라갑니다", "이번주안으로"]

    normal_keywords = ["하이", "문제", "계약체결", "전자계약", "오후", "현장계약", "문의"]

    # Preprocessing the message
    message = message.lower()

    # Check for URL
    urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)

    # Count spam and normal keywords
    spam_count = 0
    normal_count = 0
    
    for word in spam_keywords:
        spam_count += message.count(word)
    
    for word in normal_keywords:
        normal_count += message.count(word)

    # If message has URLs and more spam keywords than normal ones, classify as spam
    if urls and spam_count > normal_count:
        return True
    else:
        return False
