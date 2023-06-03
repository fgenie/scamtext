def is_spam(message: str) -> bool:
    import re

    # Check if message contains suspicious substrings
    suspicious_substrings = ["%↑", "수익실현", "추천주", "목표달성", "추천", "종목", "^^"]
    for substring in suspicious_substrings:
        if substring in message:
            return True

    # Check if message contains suspicious domains or non-spam domain with suspicious patterns
    url_pattern = re.compile(r"https?://me2\.kr/[a-z0-9]*")
    url_matches = url_pattern.findall(message)
    for match in url_matches:
        if "me2.kr" in match:
            return True

    # Check if message contains numeric values followed or escorted by non-whitespace characters
    numeric_pattern = re.compile(r"[\S]*\d[\S]*")
    numeric_matches = numeric_pattern.findall(message)
    if numeric_matches:
        return True

    return False