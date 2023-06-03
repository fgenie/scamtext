
import re


def is_spam(text):
    # Check for common spam patterns:
    # 1. URLs with .kr domain
    # 2. Percentages and upward arrows
    # 3. Repeated special characters
    # 4. Unusual long strings without spaces
    if re.search(r'https?://\S*\.kr|%', text) or re.search(r'[\^]+|(?:(?:\S{10,}))', text):
        return True
    else:
        return False


# Example usage
if is_spam("4월파이널VIP체험반"):
    print("This is spam")
else:
    print("This is not spam")

