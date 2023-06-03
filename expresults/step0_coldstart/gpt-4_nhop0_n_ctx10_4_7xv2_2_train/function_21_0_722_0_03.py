
import re

def is_spam(message: str) -> bool:
    # Check for repeated characters
    if re.search(r"(.)\1{3}", message):
        return True

    # Check if the message contains suspicious keywords or phrases
    spam_keywords = ["매매", "달성", "무료 참여", "추천", "상승", "증권사", "최종논의단계", "잔여", "월요일부터",
                     "경제적 자유", "AI 자동", "클릭", "자동 매매", "수수료", "자격 확인", "잭팟", "최고 기록", "비밀번호",
                     "초급", "심화과정", "하락", "체험반", "다음주", "남은 기회", "주식시장", "모바일쿠폰"]
    if any(word.lower() in message.lower() for word in spam_keywords):
        return True

    # Check if the message contains a URL with a suspicious domain
    if re.search(r'(http(s)?://)?(me2\.kr|ko\.gl|kakaotalk\.it|han\.gl)/', message):
        return True

    return False
