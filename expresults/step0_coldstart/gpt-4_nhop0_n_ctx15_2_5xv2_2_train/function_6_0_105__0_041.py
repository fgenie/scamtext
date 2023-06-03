def is_spam(message):
    import re

    # Pattern for detecting unwanted phrases based on the provided examples
    unwanted_phrases = [
        r'^\*',
        r'연속 [^ ]*(?:상승장|수익률검증|체험반)',
        r'(?:추천|분석|참여)(?:[^\n]*\?= http)',
        r'미래에셋증권',
        r'(수익|입장|펀\d+|안전)종목',
        r'한정수량|타점|입수|상단|급등강',
    ]

    # Combine the unwanted phrases patterns into a single regex pattern
    pattern = '|'.join(unwanted_phrases)

    # Check if the message matches the pattern
    if re.search(pattern, message):
        return True
    else:
        return False