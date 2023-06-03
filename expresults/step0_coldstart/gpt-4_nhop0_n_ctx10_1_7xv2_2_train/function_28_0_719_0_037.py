
import re

def is_spam(message):
    # Check for common spam keywords
    spam_keywords = ['무료 참여', '광고', '출시 이벤트', '챗 GPT', '해외선물', '공시발표 전', '체험반', '폭등 기법', '다음 타자', '오픈초대', '추천주', '투자상품', '오픈카톡방', '적중률']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URL patterns
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if urls:
        return True

    # Check for phone numbers
    phone_numbers = re.findall('\d{2,4}-\d{2,4}-\d{2,4}', message)
    if phone_numbers:
        return True

    # Return False if none of the spam indicators are found
    return False
