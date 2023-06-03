
import re


def is_spam(message: str) -> bool:
    spam_indicators = [
        r'\d%[\s]*↑',  # numbers with percentage sign
        r'https?:\/\/[\w]+(\.[\w]+)+',  # suspicious URLs
        r'상한가',  # potentially problematic terms in Korean (e.g., 상한가)
        r'무료거부',  # another problematic phrase in Korean (e.g., 무료거부)
        r'광고',  # another problematic phrase in Korean (e.g., 광고)
        r'[가-힣]*경력[가-힣]*',  # phrases indicating experience in Korean (e.g., 14년 된 안전한 업. 체.)
        r'[가-힣]*비용[가-힣]*',  # phrases indicating costs in Korean (e.g., "비용" 없습니다.)
        r'[가-힣]*수수료[가-힣]*',  # phrases indicating commissions in Korean
        r'[가-힣]*지원금[가-힣]*',  # phrases indicating support money in Korean
        r'\d+월\d+[가-힣]*체험반',  # phrases indicating experience periods, e.g. 4월체험반
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    return False
