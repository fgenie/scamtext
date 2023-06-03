
import re

def is_spam(text):
    # Check for common spam keywords
    spam_keywords = ["무료거부", "선물정보", "!(광고)", "투자반", "2시부터", "게임 소개", "종목상담", "최소3연상 공개", "비과세 혜택", "TG그룹", "여의도사람들"]

    for keyword in spam_keywords:
        if keyword in text:
            return True
 
    # Check for consecutive combination of characters and digits
    pattern = r"[a-zA-Z0-9]{5,}"
    if re.search(pattern, text):
        return True

    # Check for spammy URLs in the text
    spammy_urls = ["https://bit.ly", "han.gl", "me2.kr"]
    for spam_url in spammy_urls:
        if spam_url in text:
            return True

    # Check for (광고) at the beginning of the text
    if text.startswith("(광고)"):
        return True

    # If none of the conditions are met, return False
    return False

