
import re

def is_spam(message):
    # Check for common spam keywords/phrases
    spam_keywords = ["증 권 에서", "공시발표", "상한가확정", "개시예정", "귀하를", "매수하셔도", "번 오픈", "무료 이며", "멤버쉽프로모션", "횡령중", "본격화", "MOU추친중"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual number of urls
    urls = re.findall("(http(s)?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}[-a-zA-Z0-9()@:%_\+.~#?&//=]*", message)
    if len(urls) >= 2:
        return True

    # Check for excessive use of special characters
    special_chars = re.findall("[-!$%^&*@()_+|~=`{}\[\]:\";'<>?,.\/]", message)
    if len(special_chars) >= 10:
        return True

    # Check for consecutive capital letters and numbers
    capital_letters_numbers = re.findall("[A-Z0-9]+", message)
    if len(capital_letters_numbers) >= 4:
        return True

    return False
