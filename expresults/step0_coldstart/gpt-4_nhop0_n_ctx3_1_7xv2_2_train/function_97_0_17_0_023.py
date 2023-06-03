def is_spam(text):
    import re

    # Checking for spam signals in the text
    spam_signals = [
        r'\d+%',  # Numbers followed by percentages
        r'\b(slot|free|zone|promo|prize|surprise|bonus)\b',  # Common spam words
        r'\b(http|https)://',  # Links
        r'[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',  # Email addresses
        r'(.)\1{3,}',  # Repeated symbols
    ]

    # Count spam signals occurrences
    num_spam_signals = sum([len(re.findall(signal, text)) for signal in spam_signals])

    # If there are more than two spam signals, the message is considered spam
    return num_spam_signals > 2