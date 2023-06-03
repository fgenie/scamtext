def is_spam(message):
    import re

    # Check for common spam indicators
    spam_indicators = [
        r'[%0-9,.]+할인',  # discounts 
        r'(최대|최소|공시|상승|투자)[\s]*[%0-9,.]+',  # percentages or investment
        r'주식',  # stocks or shares
        r'\b[0-9]{2,}만원\b',  # amounts in 10,000 KRW
        r'(정보|공개|초대|합병|입수|특가|해당)[\s]*',  # specific terms
        r'(상한가|고급|경제|수.익|수급|재료|공시발표|초대|유.료|무료입장|고객|알려드리|기업세력|증권|납)',  # other specific terms
        r'(https?://|bit.ly)',  # urls
        r'(openkakao|kakaotalk.it|dokdo.in|me2.kr|han.gl)',  # suspicious urls
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    return False