def is_spam(message):
    # Words/phrases commonly found in spam messages
    spam_words = ["↑", "무료거부", "멤버십", "무료체험", "https://me2.kr", "비밀번호", "수익", "상승", "룰렛", "무료강의", "예약"]
    
    # Check if any of the spam words/phrases are in the input message
    for word in spam_words:
        if word in message:
            return True

    # Check if the message contains "광고" at the beginning
    if message.startswith("(광고)") or message.startswith("* (광고)"):
        return True

    # Check if the message contains excessive line breaks
    if message.count("\n") >= 3:
        return True

    return False