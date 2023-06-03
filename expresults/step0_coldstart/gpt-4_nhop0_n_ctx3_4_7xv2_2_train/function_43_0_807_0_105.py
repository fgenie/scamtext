
import re


def is_spam(message):
    # Check for any URLs with shortening services
    short_url_regex = r'(https?://(?:bit\.ly|me2\.kr|openkakao\.it).*\b)'
    short_urls = re.findall(short_url_regex, message)
    if short_urls:
        return True

    # Check for unusually high numbers such as "11만원▼" or "74,540,000"
    big_numbers_regex = r'((\d{1,3}(,|\.)?){2,}\d+|[0-9]+만원)|(▼|▲)'
    big_numbers = re.findall(big_numbers_regex, message)
    if big_numbers:
        return True

    # Check if message contains excessive section markings like "[7부]"
    section_markings_regex = r'\[\d*부\]'
    section_markings = re.findall(section_markings_regex, message)
    if len(section_markings) >= 3:
        return True

    # Check for sequences of characters that refer to specific dates
    date_regex = r'\d{1,2}일|[가-힣]{1,2}욜'
    dates = re.findall(date_regex, message)
    if len(dates) >= 2:
        return True

    # If none of the above conditions are met, consider the message as normal
    return False
