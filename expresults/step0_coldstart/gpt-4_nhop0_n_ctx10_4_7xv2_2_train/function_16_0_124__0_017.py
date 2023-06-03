
import re

def is_spam(message):
    spam_triggers = [
        {'regex': r'\b(카지노|바카라|승리|로또|홀짝|룰렛|블랙잭|스포츠토토|스포츠배팅|추천종목|적립금|민I|B.H|배-당)\b'},
        {'regex': r'http\S+', 'count': 2},
        {'regex': r'\d{5,}', 'count': 1},
        {'regex': r'(ko.t/fs|kao+.i/c[\w]+|(me2|bly|bit)\.kr/\w+)'}
    ]

    total_spam_points = 0
    for trigger in spam_triggers:
        count = len(re.findall(trigger['regex'], message))
        if 'count' in trigger:
            if count >= trigger['count']:
                total_spam_points += 1
        elif count > 0:
            total_spam_points += 1

    if total_spam_points > 1:
        return True
    return False
