
import re

def is_spam(message):
    spam_signs = [
        r'\b(https?://\S+)',
        r'\b(www\.\S+)',
        r'\b(VIP)',
        r'\b(주종/시황/뉴스)',
        r'\b(지난주 추천주)',
        r'\b(여의도사람들)',
        r'\b(차별화)',
        r'\b(실력으로 입증)',
        r'\b(선착순)',
        r'\b(늄26%↑)',
        r'\b(팜42%↑)',
        r'\b(\d+% 적중)',
        r'\b(분석/추천/시황)',
        r'\b([가-힣]{2,5}\+\+)',
        r'\b비번: \d+',
        r'\b(https?://\S+)'
    ]

    for pattern in spam_signs:
        if re.search(pattern, message):
            return True
    return False
