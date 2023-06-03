def is_spam(text: str) -> bool:
    import re
    
    # Low threshold value of spam words to consider the message spam
    spam_threshold = 2

    # List of spam words
    spam_words = ['광고', '출하합니다', '축하합니다', '이벤트', 'http', 'www', '시가총액',
                  '무료거부', '알려드린', '추천', '체험반', '신규', 'https', '오픈톡', '정보공유', '릭']

    # Function to count occurrences of spam words in the message
    def count_spam_words(text: str, spam_words: list) -> int:
        count = 0
        for word in spam_words:
            count += len(re.findall(word, text))
        return count

    # Count spam words in the text
    spam_count = count_spam_words(text, spam_words)
    
    # If the spam count is greater than or equal to the spam threshold, the message is considered spam
    return spam_count >= spam_threshold
