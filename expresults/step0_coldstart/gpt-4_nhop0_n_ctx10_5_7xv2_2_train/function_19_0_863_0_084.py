
import re

def is_spam(message):
    spam_keywords = [
        "VIP", "체험반", "고수익", "증권", "추천주", "조선", "종목", "성과", "1.5%~4.0%", "상담", 
        "조각구매", "소 액", "조선알미늄", "선입수", "인수합병", "상한가", "상당", "안내", 
        "사례금", "방산관련", "투자",
    ]
    
    patterns_to_check = [
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        r"([0-9]{1,3},)+[0-9]{3}",
        r"(\d{2}|\d{1})\s?[월|일]",
        r"\d{1,2}[.]\d{1,2}[.]\d{1,2}",
        r"\+[ ]*\d{2}%"
    ]
    
    match_found = False
    
    for keyword in spam_keywords:
        if keyword in message:
            match_found = True
            break
    
    if not match_found:
        for pattern in patterns_to_check:
            if re.search(pattern, message):
                match_found = True
                break
                
    return match_found
