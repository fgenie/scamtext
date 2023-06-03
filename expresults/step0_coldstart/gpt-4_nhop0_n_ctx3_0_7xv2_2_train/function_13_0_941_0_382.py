def is_spam(message: str) -> bool:
    import re

    # Check for consecutive special characters
    if re.search(r"(\W)\1{2,}", message):
        return True

    # Check for excessive numbers and currency or monetary expressions
    if len(re.findall(r"[0-9]+", message)) > 5 or re.search(r"(\만원|원|천원)", message):
        return True

    # Check for url shorteners or unusual domains
    if re.search(r"((http|https):\/\/)?(((\w+)(\.))+(kr|gl|me2))\/\S+", message):
        return True

    # Check for excessive capitalization
    if len(re.findall(r"[A-Z가-힣]{2,}", message)) > 3:
        return True

    return False