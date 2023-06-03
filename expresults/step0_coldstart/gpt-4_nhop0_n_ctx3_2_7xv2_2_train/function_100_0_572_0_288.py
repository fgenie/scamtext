def is_spam(text):
    """
    Function that classifies the input text as either spam or not spam.

    Args:
    text (str): The input text that needs to be classified.

    Returns:
    bool: True if the text is classified as spam, False otherwise.
    """

    import re

    # Check for a high count of special characters (e.g., '*' or '^')
    special_count = sum([1 for char in text if not char.isalnum()])
    special_ratio = float(special_count) / len(text)
    if special_ratio > 0.3:
        return True

    # Check the text for common spam clues
    spam_clues = ['축하', '당첨', '추천주', '시황', '분석', '수익률', '목표달성', '기념']
    if any(clue in text for clue in spam_clues):
        return True

    # Check for URLs preceded by symbols (e.g., 'https://me2.kr/')
    url_pattern = r'([▼\*]\s*|^)(https?:\/\/\S+|^)w{3}\.\S+'
    if re.search(url_pattern, text):
        return True

    return False