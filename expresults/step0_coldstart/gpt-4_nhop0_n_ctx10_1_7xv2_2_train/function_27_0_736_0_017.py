def is_spam(message):
    import re
    
    spam_keywords = ['목표달성기념', '추천 디젠스', '체험반', '상한가확정', '실력입증', '한농화성', 
                     '세토피아', '일만원으로', '1천만원만들기', '부자되기프로젝트', '카톡방 입장', 
                     '소니드', '최소인원으로', '9일 알려드린', '고수의 히든종목', '신청하신방 안내', '오류발생시']
                     
    shortened_url_pattern = re.compile(r'(https?:\/\/|bit(\.ly|ly)|me(\.to|2)|vvd(\.bz|bz)|han(\.gl|gl)|openkakao(\.it|it)).*')

    # Check if message contains any spam keywords
    for word in spam_keywords:
        if word in message:
            return True
    
    # Check if message contains shortened URLs
    if shortened_url_pattern.search(message):
        return True

    # If none of the spam conditions are met, the message is considered normal
    return False