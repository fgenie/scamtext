
import re

def is_spam(message):
    # Check for financial promises or large amounts of money
    money_keywords = ["만원", "천만원", "백만", "만드시기", "잔고만들기", "성공을위한투자", "부자되기프로젝트"]
    for keyword in money_keywords:
        if keyword in message:
            return True

    # Check for shortened URLs
    shortened_url_pattern = re.compile(r'(https?:\/\/\S*\.[a-z]{2,6}\/[a-zA-Z0-9]+)')
    if shortened_url_pattern.search(message) is not None:
        return True

    # Check for free promotions
    free_promotions = ["무료거부", "Vip무료체험반모집", "핵심정보를모두무료로"]
    for promotion in free_promotions:
        if promotion in message:
            return True

    return False
