import re

def is_spam(message):
    # Check for typical spam phrases and URL patterns
    spam_phrases = [
        '금일 하루만',
        '입장해 계신 톡방',
        '입장 ◆',
        '진입 예정 입니다',
        '거래 수. 수. 료.',
        '비밀 종목',
        '폭등확정',
        r'\d{4}\s+캬툒',
        '증권 에서 전달받은 고급 정보 안내입니다',
        '단타정보트레이딩'
    ]

    # Check for URLs containing suspicious patterns
    url_pattern1 = r'(https?:\/\/|me2.[~]|buly.[~]|bit\.[/]|\w+[\+]|\w+\.[~])[\w\.-]+\.[\w]+[\w\/]*'
    url_pattern2 = r'(\w{2,}\.kr\/\w{2,})'

    # Check if the message contains any of the spam phrases or suspicious URLs
    if any(re.search(phrase, message, re.IGNORECASE) for phrase in spam_phrases) or \
       re.search(url_pattern1, message) or \
       re.search(url_pattern2, message):
        return True

    return False