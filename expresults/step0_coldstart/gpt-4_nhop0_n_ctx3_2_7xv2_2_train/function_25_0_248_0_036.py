
import re

def is_spam(message):
    # check for (광고) tag in message
    if "(광고)" in message:
        return True

    # check for multiple urls in message
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if len(urls) > 1:
        return True

    # check for 대표님 in the beginning of message
    if message.startswith("대표님"):
        return True

    # check for message containing multiple percentages
    percentages = re.findall(r'\d+%+', message)
    if len(percentages) >= 3:
        return True

    # check for message containing multiple 이익, 수익, or 반환 expressions
    profits = re.findall(r'(이익|수익|환담)', message)
    if len(profits) > 1:
        return True

    return False
