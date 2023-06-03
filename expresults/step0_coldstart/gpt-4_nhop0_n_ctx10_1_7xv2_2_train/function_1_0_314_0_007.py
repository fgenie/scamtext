
import re


def is_spam(text: str) -> bool:
    # Check for typical spam phrases in the message
    spam_phrases = [
        "상한가", "추천주", "적중", "버세요", "1위", "수익률", "탈출", "상장",
        "화살표", "채팅방 종료", "통합운영", "폭락", "영입", "최소 80% 상승",
        "클릭 종목확인", "전문가 경력", "공개", "[힌트]", "목표가"
    ]

    # Check for urls and number of domains in the text
    url_pattern = re.compile(r'(https?:\/\/[^\s]+|me2\.kr|openkakao\.at)')

    urls = url_pattern.findall(text)
    domains = {url.split("//")[-1].split("/")[0] for url in urls}

    is_spam = False

    # Check if any of the spam phrases exists in the text
    for phrase in spam_phrases:
        if phrase in text:
            is_spam = True
            break

    # Then, consider it spam if there are more than 1 domains in the text
    if len(domains) > 1:
        is_spam = True

    return is_spam
