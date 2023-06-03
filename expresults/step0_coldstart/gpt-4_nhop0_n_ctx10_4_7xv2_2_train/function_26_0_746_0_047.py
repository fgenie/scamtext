def is_spam(message: str) -> bool:
    import re

    # Check for advertisement indicator at the beginning of the message
    if message.startswith("(광고)"):
        return True

    # Check for url shorteners and suspicious subdomains
    suspicious_url_pattern = r"(https?://\S*?(?:openkakao|me2|opcn-kakao)\.\S*?/)"
    if re.search(suspicious_url_pattern, message):
        return True
    
    # Check for unusual characters combinations
    suspicious_patterns = [
        r"\d{2}일",
        r"상한가",
        r"ma|M|VIP|CT",
        r"입장",
        r"적중|출발|무료거부",
        r"다음주",
        r"\d{2}%↑",
        r"수익보시고나서",
        r"신규인원",
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, message):
            return True

    return False