
import re

def is_spam(message):
    # Detect abnormal use of special characters and whitespace
    if re.search(r"[\.\-_\^\*\>\<,;]+", message):
        return True

    # Detect links
    if re.search(r"(http|https|www\.|openkakao|me2|t\.ly)\S+", message):
        return True

    # Detect numbers with % sign or 숫자만큼
    if re.search(r"\d+[%]", message) or re.search(r"\d+만큼", message):
        return True

    # Detect 연속된 한글 영문 숫자 혼용
    if re.search(r"[\d\w]+[ㄱ-ㅎㅏ-ㅣ가-힣]+[\d\w]+", message):
        return True

    # Check for common spam keywords
    spam_keywords = ["당첨", "수익", "투자", "상승", "무료거부", "최근", "매수", "익절", "상한가", "올라갑니다", "대운영", "매매", "비교", "성과", "확인", "흥미진진", "인터넷뱅킹", "추천", "재료", "고객센터"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the conditions are met, return False
    return False
