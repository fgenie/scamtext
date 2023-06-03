
import re

def is_spam(message):
    message = message.strip()

    # Check for presence of URLs
    url_pattern = "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    if re.search(url_pattern, message):
        return True

    # Check for presence of special characters
    special_chars = ["*", "_", "~", "|", "!", "#", "$", "%",
                     "&", "(", ")", "{", "}", "[", "]", "<", ">", "@"]
    counter = 0
    for char in message:
        if char in special_chars:
            counter += 1

    # Check if message has too many special characters
    if counter / len(message) > 0.1:  # Adjust this threshold as needed
        return True

    # Check for consecutive capital letters
    caps_pattern = "[A-Z]{3,}"
    if re.search(caps_pattern, message):
        return True

    # If none of the above conditions are met, the message is not spam
    return False
