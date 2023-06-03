
import re

def is_spam(message):
    # Convert the message to lower case
    message = message.lower()

    # Some common spam characteristics
    spam_words = ["추천주", "공시발표", "성공수익", "극비", "미공개", "신청하신", "선정되셨습니다."]
    url_pattern = "https?:\/\/\S+\.\S+"
    phone_number_pattern = "\d{2,4}-\d{2,4}-\d{2,4}"
    excessive_special_characters = r"[\!@#$%^&*]{3,}"
    excessive_numbers = r"\d{5,}"
    
    # Check if the message contains common spam words
    for word in spam_words:
        if word.lower() in message:
            return True

    # Check if the message contains a URL
    urls = re.findall(url_pattern, message)
    if urls:
        return True

    # Check if the message contains a phone number
    phone_numbers = re.findall(phone_number_pattern, message)
    if phone_numbers:
        return True

    # Check if the message contains excessive special characters
    if re.search(excessive_special_characters, message):
        return True

    # Check if the message contains excessive numbers
    if re.search(excessive_numbers, message):
        return True

    # If none of the above criteria is met, the message is not spam
    return False
