
import re


def is_spam(message: str) -> bool:
    # Check for typical spam phrases
    spam_phrases = [
        "광고",
        "투자",
        "수익",
        "주식",
        "이익",
        "무료",
        "확인",
        "사세요",
        "보상",
        "보장"
    ]

    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for links
    link_pattern = re.compile(r"http[s]?://\S+")
    if link_pattern.search(message):
        return True

    # Check for phone numbers
    phone_pattern = re.compile(r"[\d]{2,4}-[\d]{3,4}-[\d]{4}")
    if phone_pattern.search(message):
        return True

    return False


# Test the function
# Note that this section is just for testing and should not be added to the actual implementation

spam_messages = [
    "(광고)㈜SP\n안녕하세요",
    "(광고)3일 연속 VI 적중!!\n↓급등예정 종목 확인↓\n\nhan.gl/hDpebP\n\n\n무료수신거부0808550",
    "(광고)\n 나만몰랏네\n하는 사람은근많네",
]

normal_messages = [
    "돈 많이벌고싶당",
    "스팸이 무서워...\n매일 날아와",
    "아아.. 어떡하지?",
    "하이",
    "하이",
    "관리비 입금해드렸습니다. 확인 부탁드립니다!",
    "송장번호 : 1234-5678-1234\n■ 보내는분 : 리빙스토리 남양주 오\n■ 상품명 : 올스텐가위",
    "수익 축하한다 다음은 어디?",
]

for msg in spam_messages:
    print(is_spam(msg))  # Should print True

for msg in normal_messages:
    print(is_spam(msg))  # Should print False
