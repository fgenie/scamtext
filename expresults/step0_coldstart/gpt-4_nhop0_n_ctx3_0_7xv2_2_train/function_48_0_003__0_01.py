def is_spam(message):
    spam_keywords = ['% 수익달성', '슈퍼개미', '부자가 된', '카카오톡 공개 공부방', '시작해서', '최대 69% 할인', '무료수신거부', '오픈채팅방', '자동입장', 'buly.kr', 'me2.kr']
    normal_keywords = ['SKT', 'T deal', '종근당건강', '무료배송', '프로메가 오메가3', '무료 수신거부']
    
    message_keywords = message.split(' ')

    spam_score = 0
    normal_score = 0

    for word in message_keywords:
        if word in spam_keywords:
            spam_score += 1
        if word in normal_keywords:
            normal_score += 1
    
    return spam_score > normal_score