def is_spam(text: str) -> bool:
    import re
    
    # Check for url shorteners
    url_shorteners = re.compile(r'(?:https?://)?(?:me2\.kr|openkakao\.at)/\S*')
    if url_shorteners.search(text):
        return True

    # Check for keywords associated with spam messages
    spam_keywords = re.compile(r'(추천|상한가|목표달성|일정|계약|호재|테마주|촉매|차트|일주일|급등주|스윙주)')
    if spam_keywords.search(text):
        return True

    # Look for repeated keywords and symbols
    regex_repeated_patterns = re.compile(r'(.)\1{3,}')
    if regex_repeated_patterns.search(text):
        return True

    # Check for percentage increases or any other financial related terms
    percentage_terms = re.compile(r'(\+|-)?\d+(\.\d+)?%')
    if percentage_terms.search(text):
        return True

    return False