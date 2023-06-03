
import re

def is_spam(message):
    # Check for percentages or gains
    if len(re.findall(r'(\d+%|\d+달성|\d+이익)', message)) > 0:
        return True
    
    # Check for promises of earnings or benefits
    if any(x in message for x in ['무료입장', '특별정보방', '상담']):
        return True

    # Check for links that are suspicious
    if 'openkakao' in message and len(re.findall(r'(◆.+◆)', message)) > 0:
        return True
    
    # Check for too many urgency phrases
    if len(re.findall(r'(신규|최고|출시)', message)) > 1:
        return True

    # Check for financial or investment content
    if any(x in message for x in ['주식', '평생무상', '최대']):
        return True

    return False
