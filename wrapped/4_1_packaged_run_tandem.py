import importlib
from pathlib import Path
import pandas as pd
from typing import Callable, Sequence, Mapping, Any, Union
import re
from fire import Fire
'''
input: 3_inputmsgs.csv (sequence of sms)
output:
    - if decision_only=True
        sequence of boolean decisions (spam true or not)
    - else
        json like object containing decisions 
        
        ```else output example
        response = dict(
            input_txts = input_txts, # input_txts to be diagnosed (inputs)
            voted_spam_fraction = voted_spam_ratio, # fraction of functions that consider each msg is spam.
            decisions = decisions, # is_spam
            num_functions = num_functions,  # number of functions used to decide whether it's a spam       
        )
        ```

'''

def evaldirs(conf):
    evaluate_dirs = (Path(conf.root)/conf.expname).glob(f"{conf.globpattern}{conf.data}*")  
    return [p for p in evaluate_dirs]

def tandem_execution(functions:Sequence[Callable], txt:str)->float:
    # print([func(txt) for func in functions])
    results = pd.Series([func(txt) for func in functions]).mean()
    return results

def preproc(txts:Sequence[str])->Sequence[str]:
    # preproc for engine (as experimented)

    # erase normal urls, typical headers that hide real patterns (e.g. [Web발신, 국외발신, 국제발신])
    headers = ['[Web발신]', '[국외발신]', '[국제발신]']
    headers_pattern = "|".join(map(re.escape, headers)) 
    url_pattern = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

    processed_txts = [ re.sub(headers_pattern, "", re.sub(url_pattern, "", txt)) for txt in txts]
    newtxt = re.sub(url_pattern, "", txts[0])
    newtxt = re.sub(headers_pattern, "", txts[0])
    
    return processed_txts

def main(
        inputmsgs_csv:str='3_inputmsgs.csv',
        decision_only=False, 
        thld:float=0.35, # affects performance. do not configure this.
        )->Union[Mapping[str,Any],Sequence[bool]]:
    # load checkers
    indiv_checkers = []
    # print('loading')
    for p in Path().glob('funcs/f_*.py'):
        # print('\t', str(p))
        module = importlib.import_module(str(p.parent/p.stem).replace('/', '.'))
        indiv_checkers.append(module.is_spam)
    # load input_txt msgs
    input_txts_ = pd.read_csv(inputmsgs_csv).msgs.tolist() #raw
    input_txts = preproc(input_txts_) # preproc
    voted_spam_ratio = [tandem_execution(indiv_checkers, txt) for txt in input_txts]
    decisions = [r>=thld for r in voted_spam_ratio]
    num_functions = len(indiv_checkers)
    
    if decision_only:
        response = decisions 
    else: 
        response = dict(
            input_txts = input_txts_, # processed input to the checkers
            voted_spam_fraction = voted_spam_ratio, # fraction of functions that consider each msg is spam.
            decisions = decisions, # is_spam
            num_functions = num_functions,  # number of functions used to decide whether it's a spam       
        )
    
    return response
    


if __name__ == "__main__":
    Fire(main)

'''
실행 결과


input_txts:          ["[Web발신]\n[프리미엄콘텐츠] 미국주식 사관학교 1개월 이용권 3,900원이 결제되었습니다.", "[Web발신]\nYour Beam verification code is: 5557", "[국외발신]\nG-592238 is your Google verification code.", "[Web발신]\n[아프리카TV] 인증번호 [11382]를 입력해 주세요.", "[Web발신]\n[민방위 교육센터]\n본인확인을 위해 인증번호 [514073]를 입력해 주세요.", "[Web발신]\n[한전사이버지점]고객님의 한전정보 SMS 인증번호는[290017]입니다.", "[Web발신]\n[삼성카드]SMS 인증번호[471636]", "[한국모바일인증(주)]본인확인 인증번호[995988]입니다. \\타인 노출 금지\\\"\"", "[Web발신]\n[MY COMPANY] 승인\n3101 손선일님\n134,000원 일시불\n신세계센트럴시티\n잔여한도1,866,000원", "[Web발신]\n[MY COMPANY] 현대카드 당월 결제 예정 금액 안내\n\n회원님, 당월 법인카드 결제 예정 결제금액을 안내 해드립니다\n\n[상세 안내]\n- 대상카드 : 3101 카드\n- 결제 예정 금액 : 49,700원 (05/07 기준)\n- 결제일 : 05/24\n- 납부방식 : 농협중앙\n\n. 상세내역은 청구서 또는 현대카드 법인홈페이지에서 확인이 가능합니다.\n\n[문의] 1577-6000", "[국외발신]\n손선일님\n[수입세금]\n발생되였습니다.\n금액892,624원\n사건코드(3**4)\n금일 자동처리예정\n민원0269569423", "https://www.youtube.com/live/garRuI-ex6w?feature=share\n주일낮예배입니다", "[Web발신]\n(광고)크린토피아 내일까지! 패딩,점퍼,스웨터,코트,겨울조끼 세탁15%세일! 무료거부0807450061", "[여신금융협회] 본인확인 인증번호[506382]를 화면에 입력해주세요", "[CJ대한통운]고객님의 상품(568830418273)이 배송되었습니다.▶인수자(위탁):문앞"]
voted_spam_fraction: [0.2916666666666667, 0.2222222222222222, 0.25, 0.20833333333333334, 0.2777777777777778, 0.2777777777777778, 0.2222222222222222, 0.3194444444444444, 0.3472222222222222, 0.4444444444444444, 0.4583333333333333, 0.05555555555555555, 0.75, 0.2361111111111111, 0.3194444444444444]
decisions:           [False, False, False, False, False, False, False, False, False, True, True, False, True, False, False]
num_functions:       72
'''