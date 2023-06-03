import re

def is_spam(message):
    pattern_1 = re.compile(r"[.!]*[a-zA-Z0-9.+_$&#%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z][a-zA-Z.]*")
    pattern_2 = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    pattern_3 = re.compile(r"\d{1,3},\d{3}(?:,\d{3})*원")
    pattern_4 = re.compile(r"([A-Za-z0-9+._-]+bit\.[A-Za-z0-9+_%=-]\S+)")
    pattern_5 = re.compile(r"[A-Za-z0-9%+=-]+[.]+[a-zA-Z]")

    if bool(pattern_1.search(message)) or bool(pattern_2.search(message)) or bool(pattern_3.search(message)) or bool(pattern_4.search(message)) or bool(pattern_5.search(message)):
        return True
    else:
        return False