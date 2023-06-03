def is_spam(text: str) -> bool:
    import re

    # Conditions to classify messages as spam
    spam_conditions = [
        # Multiple words combined without spaces
        lambda txt: re.search(r'[A-Za-z\d]+[^\x00-\x7F]+[A-Za-z\d]+', txt),
        # Consecutive special characters
        lambda txt: re.search(r'[\W_]{3,}', txt),
        # Repeated phrases or links
        lambda txt: re.search(r'(.{10,}?)\1+', txt),
        # Link with non-standard prefix
        lambda txt: re.search(r'https?:\/\/\w+([^.])', txt),
        # Upper case words (use sparingly)
        # lambda txt: re.search(r'\b(?:[A-Z]+\S*){3,}', txt),
    ]

    return any(condition(text) for condition in spam_conditions)

# Note: As requested, test usage should not be added after the implementation.
# However, for best results, you should test and adjust the 'spam_conditions' to match your specific use case.