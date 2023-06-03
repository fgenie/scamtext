def is_spam(message: str) -> bool:
    import re

    # Check for typical spam elements like url shorteners, an excessive amount of symbols, and specific keywords.
    url_shorteners = re.findall(r"(http?s?:?//me2\.kr|http?s?:?//han\.gl)", message)
    excessive_symbols = re.findall(r"(\s\W{2,}\s)", message)
    spam_keywords = re.findall(r"(지니틱스|나노 수익|slot|콤0.8%|페백10%|급등예정)", message)

    # If any of the above spam indicators are present, the message is considered spam.
    if bool(url_shorteners or excessive_symbols or spam_keywords):
        return True
    else:
        return False