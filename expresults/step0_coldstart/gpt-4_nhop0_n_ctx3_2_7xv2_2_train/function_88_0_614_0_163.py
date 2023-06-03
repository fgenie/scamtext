def is_spam(message: str) -> bool:
    import re
    
    # Check for multiple exclamation points, question marks, or special characters
    if re.search(r"[!?.]{2,}", message) or re.search(r"[@#&%$]{2,}", message):
        return True
    
    # Check for a high number of consecutive capital letters
    if re.search(r"[A-Z]{4,}", message):
        return True
    
    # Check for words typically associated with spam, such as "광고" or "링크"
    spam_keywords = ["광고", "링크", "클릭", "카톡방", "수익", "적중", "상담하기", "프로젝트", "무료거부", "오픈", "종목", "익절"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for a high percentage of alphanumeric and special characters
    num_alphanumeric = sum(c.isalnum() for c in message)
    num_special_characters = sum(not c.isalnum() and not c.isspace() for c in message)
    if num_special_characters / (num_alphanumeric + num_special_characters) > 0.25:
        return True

    return False