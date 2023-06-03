
import re

def is_spam(message):
    spam_phrases = [
        '오후2시에 대형공시 발표확정',
        '비용 일체 없습니다',
        '거짓된 수.익으로 현혹하지 않습니다',
        '종.목을 남발하지 않습니다',
        '언급한 종.목은 끝까지 대응합니다',
        '목표가 : 31,000원이상',
        '수익나는걸 보실수있으니',
        '한번들어와서 확인만하고 나가셔도 됩니다',
        '첫 입 3o ％',
        '첫 출 까지 무/한 20%',
        '새고객1콩',
        '입 hhs11',
        '첫 입 3－０ ％',
        "www.nbet02.com"
    ]

    # Iterate over spam phrases and create a regex pattern to match them.
    spam_phrases_pattern = ['(.*{})'.format(re.escape(phrase)) for phrase in spam_phrases]

    for pattern in spam_phrases_pattern:
        if re.match(pattern, message):
            return True

    return False
