
import re

def is_spam(message):
    message = message.lower()
    
    spam_signals = [
        r'http[s]?:\/\/\S+',
        r'\b(?:\d{1,2}[%]|[ㄱ-ㅎㅏ-ㅣ가-힣a-z\d]{2,6}[추청체매시])(?:매도)?\b',
        r'\b(?:하는|되는|갈|일부|유투브)+\b',
        r'\b(?:기보시신겁|종목|금일|지금|딱|계셔도|느낄수|구경해보세)+\b',
        r'\b(?:달성|격상에|폭등|조조|아프리카|세토피아)+\b',
        r'\b(?:정확|성공시|습득해|아름|보유중이신)+\b',
        r'\b(?:어려운게|진행중에)+\b'
    ]
    
    for signal in spam_signals:
        if re.search(signal, message):
            return True
    
    return False
