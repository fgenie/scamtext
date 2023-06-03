
import re

def is_spam(message):
    # Check for presence of numbers and special characters
    special_char_count = len(re.findall(r'\W', message))
    digit_count = len(re.findall(r'\d', message))

    # Check for presence of suspicious links
    suspicious_links = re.findall(r'(http|https):\/\/[\w\.-]+(?:\/\S*)?', message)

    # Check for presence of suspicious keywords
    spam_keywords = ['상한가확정', '노후 자금', 'AI사업']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If more than 40% of the message contains special characters or digits, it is likely spam
    if special_char_count + digit_count > len(message) * 0.4:
        return True

    # If the message contains suspicious links, it is likely spam
    if len(suspicious_links) > 0:
        return True

    # If none of the above conditions are met, the message is likely not spam
    return False
