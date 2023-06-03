
import re

def is_spam(message):
    # Check for common spam features
    message_lower = message.lower()
    spam_features = [
        r'\d+',                                              # Has numbers
        r'\b(http:\/\/|https:\/\/)(\w+\.?)+\b',             # Has URLs
        r'\bopenkakao.it\/\w+',                             # Has specific URLs
        r'\bbit.ly/',                                       # Has specific URLs
        r'\bme2.kr/',                                       # Has specific URLs
        r'\b\w{4}\s*\d{1,2}(월|주차|일)',                     # Has specific date pattern
        r'[0-9,]+(수익|월 총 수익|최근 \d+개월 매매 성과|십만척|원 가입성공 예약)', # Has specific pattern with numbers
        r'\bvip\b',                                         # Has 'VIP' pattern
        r'\b무료체험반\b',                                    # Has '무료체험반' pattern
        r'\b상한가\b',                                      # Has '상한가' pattern
        r'▼.*▼',                                            # Has specific symbols pattern
    ]

    for feature in spam_features:
        if re.search(feature, message_lower):
            return True

    # No spam features found
    return False
