
import re

def is_spam(text):
    # Check for multiple short URLs or suspicious domains
    url_pattern = re.compile(r'(https?://\S+|bit\.ly/\S+|me2\.kr/\S+|vvd\.bz/\S+|han\.gl/\S+|openkakao\.at/\S+)')
    urls = url_pattern.findall(text)
    if len(urls) > 1:
        return True

    # Check for numbers followed by won (Korean currency), percentage signs, or up arrows
    money_pattern = re.compile(r'(\d+(,\d{3})*(원|₩|%|↑))')
    if money_pattern.search(text):
        return True

    # Check for phrases common in spam messages
    spam_phrases = ['목표달성기념', '추천주 현황', '극비 정보', '차별화 된', '신청하신 방에 당첨 되셨습니다']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # If none of the above conditions are met, the message is not spam
    return False
