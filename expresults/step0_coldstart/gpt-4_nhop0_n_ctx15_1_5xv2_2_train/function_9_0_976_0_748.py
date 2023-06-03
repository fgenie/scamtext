def is_spam(message: str) -> bool:
    import re

    # Check for common spam phrases or patterns
    spam_phrases = [
        r"카카오톡제재", r"테|_|\(|\)|£|€|\.| |그램으로 이동", r"\d월.험반", r"잔여 [\d]+/",
        r"신년맞이 모집", r"무료거부", r"\d+일 알려드린", "신 청 하 신", "인증\w+", "클릭",
        r"openkakao.at|me2.kr|vvvkauy.com|ocx.kr|a.to", r"\d%.상승",
        r"사만 원", r"지니틱스", "지금 날짜", r"폐.배터리"
    ]

    # Check for excessive use of special characters
    special_chars = [r"\.{2,}", r"!{2,}", r"\?{2,}", r"♥"]

    # Define a threshold for special characters as a percentage of the total message length
    special_char_threshold = 0.25

    # Combine spam phrases and patterns into a single regex pattern
    spam_regex = "|".join(spam_phrases + special_chars)
    matches = re.findall(spam_regex, message)

    # Count the number of special characters found
    special_char_count = sum(len(match) for match in matches if match in special_chars)

    # If any spam phrases or patterns are found or the special character count exceeds the threshold, return True
    if matches and special_char_count / max(1, len(message)) <= special_char_threshold:
        return True

    # If none of the checks above matched, return False
    return False