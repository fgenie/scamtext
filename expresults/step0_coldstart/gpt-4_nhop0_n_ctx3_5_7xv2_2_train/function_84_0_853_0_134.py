
import re


def is_spam(message):
    # Spam characteristics to look for:
    spam_pattern = [r"[별|배|▶|★|(클릭)|▼]",
                    r"\d{1,2}[월|배]",
                    r"(목표가|종목|종.목|폭등예상|수익)",
                    r"http[s]?://\S+",
                    r"오후\d{1,2}시",
                    r"움직이시는 분",
                    r"무료체험"]

    # Check for the presence of spam characteristics in the input message
    for pattern in spam_pattern:
        if re.search(pattern, message):
            return True

    # If no spam characteristics are found, classify the message as not spam
    return False
