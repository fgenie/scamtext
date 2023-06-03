def is_spam(text):
    import re
    
    # Checking if the message contains typical spam phrases
    spam_phrases = ["당첨", "무료입장", "수익", "클릭후", "입장", "증권사", "약속합니다", "상한가", "축하합니다",
                    "관찰해보시", "추천드리는", "폭등", "공시공개", "오픈초대", "단체방", "계약금",
                    "경제야 놀자 TV", "유료전환"]

    for phrase in spam_phrases:
        if phrase in text:
            return True
    
    # Checking for the presence of multiple URLs
    urls = re.findall(r'(https?://\S+)', text)
    if len(urls) >= 2:
        return True
    
    # Checking for presence of money-related terms and numbers
    money_terms = ["원", "KRW", "실현수익률", "수익률", "\\+\\d+%"]
    for term in money_terms:
        if re.search(term, text):
            return True
    
    return False