def is_spam(text: str) -> bool:
    import re
    
    keywords = ['급등예정', '골드해선그룹', '광고', '읠장', '신청', '실. 제. 성. 과.', '지원금', '무료거부', '상한가', '무상', '유.료전환', '특별정보방', '특별한 혜택']
    spam_formats = [
        r"^\*\s*[\s\S]*[가감녀녕니다라마바사아자차카타파하]\s*(?:https?://\S+|openkakao\.\S+|(?:gg\.gg|me2\.kr)/\S+)",
        r"\d{4,}\%{1}",
    ]

    text = text.strip()

    # Check for excessive special characters and keywords
    special_char_count = sum(1 for c in text if not c.isalnum() and c not in " \t\n")
    if special_char_count / len(text) > 0.3:
        return True

    for kw in keywords:
        if kw in text:
            return True

    for sf in spam_formats:
        if re.search(sf, text, flags=re.MULTILINE | re.IGNORECASE) is not None:
            return True

    return False