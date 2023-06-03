
import re

def is_spam(message):
    # Checks for common spam keywords (case insensitive)
    keywords = re.compile(r'''(신약개발관련주|상한가확정|루멘스|오픈|수익|단독발표정보
                                |추천|투자|체험반|FDA|입증|수익|참여
                                |매집|마감|텍, 권)
                              ''', re.VERBOSE | re.IGNORECASE)
    if keywords.search(message):
        return True

    # Checks for any suspicious URLs and phone numbers in the message
    urls = re.compile(r'(http(s)?\://)?(www\.)?(\w+\.\w{2,3})')
    phone_numbers = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')
    if urls.search(message) or phone_numbers.search(message):
        return True

    return False
