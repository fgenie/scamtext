def is_spam(message):
    import re

    # Check for excessive special characters
    special_chars = r"[<>%!?#()]"
    count_special_chars = len(re.findall(special_chars, message))
    if count_special_chars > 10:
        return True

    # Check for short links
    short_link_pattern = r"(https?://)?(\w{2,5}\.)\w{2,5}(/\w{0,10})?"
    has_short_link = bool(re.findall(short_link_pattern, message))
    if has_short_link:
        return True

    # Check for common spam words
    spam_words = ["FDA", "지원", "추천", "상한가", "수익", "최고", "증권", "종목", "특별", "공개", "관련주", "선물", "스튜디오",
                  "특별정보방", "원하는", "정부", "약관", "수상내역", "친구추가", "물려있는", "무.료", "상담", "VIP", "응원", "이벤트"]
    for word in spam_words:
        if word in message:
            return True

    # Check for excessive capital letters
    count_capital_letters = sum(map(str.isupper, message))
    if count_capital_letters > 50:
        return True

    return False