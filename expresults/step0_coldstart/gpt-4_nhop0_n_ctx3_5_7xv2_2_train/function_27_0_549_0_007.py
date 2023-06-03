
import re


def is_spam(message: str) -> bool:
    # Check for shortening URL services (e.g. bit.ly, me2.kr, vo.la)
    url_pattern = r"(https?:\/\/)?(bit\.ly|me2\.kr|vo\.la)\/\S+"

    # Check for suspicious percentage numbers (e.g. 30%↑, 3연상폭등)
    percentage_pattern = r"(\d{1,2}%[\s\W]*\↑|[\s\d]+연상폭등)"

    # Check for suspicious financial and investment related terms (e.g. 상한가확정, 추천주, AI사업본격화)
    financial_terms_pattern = r"(상한가확정|추천주|AI사업본격화|[A-Z]상장기업|MOU추친중)"

    # Check if any of the suspicious patterns are found in the message
    if re.search(url_pattern, message) or re.search(percentage_pattern, message) or re.search(financial_terms_pattern, message):
        return True
    else:
        return False
