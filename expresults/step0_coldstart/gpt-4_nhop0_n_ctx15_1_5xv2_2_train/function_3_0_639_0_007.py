
import re

def is_spam(message: str) -> bool:
    # Check for suspicious keywords
    spam_keywords = ["상한가", "상담하기", "적중완료", "준법감시인", "보상 하겠습니다", "분석,상담,진단", "개구리핵심정보",
                     "클릭률", "확정", "모바일서비스 이용중지", "10분 외", "추첨", "주식비결", "무상", "신규정보", "거래량 폭등", "증 권", "전략 마감임박", "직접판단하세요", "수익률", "연 금"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs with suspicious formats
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, message)

    for url in urls:
        suspicious_formats = ["me2.kr", "bit.ly", "openkakao", "buly.kr", "vo.la", "ko.gl", "opcn-kakao.com", "me.shinhan", "me2.kr", "openkakao.at"]
        for format in suspicious_formats:
            if format in url:
                return True

    # Check for multiple special characters, indicative of links
    special_chars = ["+", "*", "#", "%", "$", "@", "&"]
    special_char_count = sum([message.count(char) for char in special_chars])
    if special_char_count >= 3:
        return True

    return False
