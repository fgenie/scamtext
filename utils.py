import tiktoken
from typing import List, Tuple, Sequence, Any
import numpy as np
import pandas as pd


def eval_on_unseen_train(
    func=None,
    spams:Sequence[str]=None,
    normals:Sequence[str]=None,
    n_context_examples:int=-1     
)->Tuple[float, float, str, str]:
    assert func is not None
    assert spams is not None 
    assert normals is not None
    assert n_context_examples >= 0
    assert n_context_examples<len(spams) and n_context_examples<len(normals)
    
    spams, normals = map(pd.Series, [spams, normals])
    tp_1, tp_2 = spams.apply(func).sum(), len(spams) 
    fp_1, fp_2 = normals.apply(func).sum(), len(normals)
    tp = (tp_1-n_context_examples) / (tp_2-n_context_examples)
    tpmsg = f"{tp_1-n_context_examples} / {tp_2-n_context_examples}"
    fp = (fp_1-n_context_examples) / (fp_2-n_context_examples)
    fpmsg = f"{fp_1-n_context_examples} / {fp_2-n_context_examples}"

    return round(tp,3), round(fp,3), tpmsg, fpmsg

def refine_code(code:str):
    if "```python" in code:
        print('refine_code was actually needed!')
        code = code.split('```python')[1]
        code = code.split('```')[0]
    return code

def make_minibatches(whole:Sequence, bsz=10)->Sequence[Sequence]:
    batched = [whole[start:start+bsz] for start in range(0, len(whole), bsz)]
    if len(batched)>1:
        if len(batched[-1])< len(batched[-2]):
            batched.pop() # remove dangling minibatch to improve prompt quality
    return batched

def count_token(txt, model='gpt-4'): # gpt-3.5-turbo
    # returning 0 if txt is not a string
    enc = tiktoken.encoding_for_model("gpt-4")
    return len(enc.encode(txt)) if isinstance(txt, str) else 0


def get_exerpt(longtxt:str, toklength:int=80, delim:str='\n')->Tuple[str, int]:
    # if the message is too long, divide it into pieces and pick one as its representation.
    if delim not in longtxt:
        return longtxt

    spls = longtxt.split(delim)
    spl_lens = [count_token(sp) for sp in spls]
    indices, newlengths = chunk_lengths(spl_lens, threshold=toklength)
    pick = np.random.randint(len(indices))


    span = indices[pick]
    l:int = newlengths[pick]
    excerpt:str = "\n".join(spls[span[0]:span[1]+1])
    # print(f"{spls=}")
    # print(f"{indices=}")
    # print(f"{newlengths=}")
    # print(f"{pick=}")
    # print(f"{excerpt=}")
    return excerpt, l
   


def chunk_lengths(lengths: List[int], threshold: int) -> Tuple[Sequence[Tuple[int, int]], Sequence[int]]:
    def variance(l: List[int]) -> float:
        return abs(sum(l) - threshold)

    i = 0
    merged_indices = []
    new_lengths = []

    while i < len(lengths):
        current_chunk = [lengths[i]]
        j = i + 1

        if j < len(lengths):
            temp_chunk = current_chunk + [lengths[j]]
            if variance(temp_chunk) <= variance(current_chunk):
                current_chunk = temp_chunk
                merged_indices.append((i, j))
                i = j + 1
            else:
                merged_indices.append((i, i))
                i = j
        else:
            merged_indices.append((i, i))
            i = j

        new_lengths.append(sum(current_chunk))

    return merged_indices, new_lengths


txt='''
"[Web발신]
지난주 추천주 현황
-더메티팜42%↑
-조선알미늄26%↑

3주차 종목 내일부터
https://me2.kr/mjp

[Web발신]
금일부터 ""4월VIP투자반"" 시작
차별화 된 분석/추천/시황
실력으로 입증
https://me2.kr/mjp
▲

[Web발신]
""이방법 하나면
100,000원 으로
주 2,720,000원 성공
무료체험▼
https://dokdo.in/p7

[Web발신]
여의도사람들4월체험반
https://me2.kr/mjp
-정확한 분석/타점
-검증된 수익률
-종목상담/추천

[Web발신]
18일 긴급입수정보
C제약, 탈모치료제 국내식약처 정식허가임박
상한가 확정
https://me2.kr/mjp

[Web발신]
정보방 안내

초대해드립니다!
200받고 시작하세요

https://vvd.bz/b8W0

[Web발신]
FROG 4월3주차VIP무료체험반
15년 연혁의 청개구리핵심정보를 모두 무료로!
https://me2.kr/tlk

[Web발신]
오후부터 시작하는 VIP체험반입니다
여의도부장들의 타점/분석을 한눈에!
https://me2.kr/bk2"'''
# print(txt)
# for i in range(3):
#     print(get_exerpt(txt))

# test chunk_lengths
# lengths = [4, 5, 20, 3, 12, 3, 10]
# threshold = 12
# indices, new_lengths = chunk_lengths(lengths, threshold)

# print("Indices:", indices)
# print("Lengths:", new_lengths)




# TXT = '''- [국제발신]
# slot🎰zone

# ☝처음혜택
# 10 +3O% +2

# 🍀매일첫 +15%

# 💞(콤0.8%,페백10%)

# ⓢlⓩ102.com
# - [Web발신] 금값 사상 최고가 경신 30만 시작 1780만 마감
# - [Web발신]
#  님

# 신 청 하 신 

# 입장 안내 드립니다.

# openkakao.io/Wscz
# - [Web발신]
# bit.ly/3KGQVIV
# vip주,식 세,력 단,타 1일1매도
# 무료방 입니다
# 3일만 지켜보세요
# - 지난주 추천주 현황
# - 단타정보트레이딩
# - 샌즈 vip 단타 폭등 기법 아줌마 비밀 공시공개 오픈초대 해선 단체방
# - [Web발신]
# (광고)특별찬스잡으세요

# ▒  대형  Major 『 명-가 』
# ****************************
# ▒ 세계 NO.1 초l고 ㅂ.H당
# ****************************

# ★★★★★★★★★★★★★

#  ▶ LIVE CA.ㅈl노 적립금

#     => ㅂ.H팅 금액 1% 적립 ♥

#  ▶ 각종 ㅁlㄴl GAME

#      => 1 . 9 8  ㅂ.H당 ♥

#  ▶ 바［CA］ㄹ.r

#      => 2 . Θ 1 ㅂ.H당 ♥

#  ※ 꼭 비교 한번 부탁드립니다

# ★★★★★★★★★★★★★

# ▩ 메가 C.A.S.H 드랍 
#          ↓   ↓   ↓
#   매일매일 １ΟΟ 만원 지급
#   ￣￣￣￣￣￣￣￣￣￣￣￣
# ▩ 처 음 방 문 시  ♥
#          ↓   ↓   ↓
#    3+2  5+3  10+5  20+7
#   ￣￣￣￣￣￣￣￣￣￣￣
#    30+10 50+15 100+30
#   ￣￣￣￣￣￣￣￣￣￣￣

#  ※ 게시판 필히 확인해주세요.

#  ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝

# 【 명-가 】 새 가족분들을 위해
# 준비한 것들을 꼭 받아가세요

# ▶방문 :  mⓖ-zxc.com

# ▶Key  :  3030

#  ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝

#  ♥ 준 비 된 게 임 들
#     ￣￣￣￣￣￣￣￣
#  ※ 실..시..간..라..이..브

#  ※ 에..볼..루..션

#  ※ 동..행..가..상

#  ※ 미..니..게..임

#  ※ M쥐M & LO투S

#  ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝

# ※ 불편한 규정과 제재를 과감히
#    없에 버렸습니다

# ※ (유)출 및 (조)작 등 헛소리를
#    하지 않겠습니다

# ※ 충(환)에 있어 빠르고 신속하게
#    대처하겠습니다

# ※ 멈춰있지 않고 항상 새로운
#    이벤트들을 제공하겠습니다

#  ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝

# 【 명-가 】 새 가족분들을 위해
# 준비한 것들을 꼭 받아가세요

# ▶방문 :  mⓖ-zxc.com

# ▶Key  :  3030

#  ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝ ＝

# ㉿±∏Θ¾


# 무료수신거부 0808550128
# 인증번호 628
# - [Web발신]
# 님

# 신 청 하 신 

# 입장 안내 드립니다.

# openkakao.io/Wscz
# - [Web발신]
# 님
# 신청하신 방 
# 입장 하시길 바랍니다

# kakaotalk.it/E8sc
# - [Web발신]
# 님 신청하신 방
# 입장 안내 드립니다

# kakaotalk.it/gd7q
# - [Web 그룹]
# 상상그룹
# 카>에볼go.com

# 지>신규감사쿠폰

# 노>신규 5만원
# - [Web발신]
# 선 물 옵 션
# 경제적 자유를향해
# 초심부터 심화과정 교육
# ▼단 하루 입장▼
# fste.in/hsh2
# - 축하합니다, 신청하신 VIP에 선정되셨습니다.
# 언론사 미공개 공시종목 공개
# 극비 작전주 선착순 공개
# - [Web발신]
# 라칸★

# 매일15%콤퓨2%

# 처음40%
# 주1회=BBQ+피자+활쿱
# 전화X

# 톡uo119
# abit.ly/itxja
# 코드:자동
# - 네
# - [Web발신]
# [채팅방 종료안내]
# *통합운영
# *500명 제한참여
# *기존정보/혜택유지
# ▼▼
# http://신규통합방.com
# - [Web발신]
# (광고)
# 이효식매니저
# 신년맞이 모집
# 비트/단타거래
# ocx.kr/3gYlA
# 암호1133
# 무료거부  0801364481
# - [Web발신]
# 만원으로 백만원 달성
# url.kr/xcul67
# '''

# EN = """Act as a skilled programmer using regex to process massive bunch of text data. Please write a python function that correctly classifies the above spam messages from the normal ones. Mind that the function should not overfit to the examples above. The name of the function is <code>is_spam</code>. Be cautious not to detect them whether they starts with [Web발신] or not. You don't need to implement the test code of it."""
# CODE = '''

# def is_spam(text):
#     # Define regular expressions to match common patterns in spam messages
#     regex_list = [
#         r'http\S+',  # URLs
#         r'[가-힣]*[A-Z]+[가-힣]*',  # Korean text including English words in all caps
#         r'\d{4}년\d{1,2}월\d{1,2}일',  # Date in the format of YYYY년MM월DD일
#         r'\d{1,2}:\d{1,2}:\d{1,2}',  # Time in the format of HH:MM:SS
#         r'상한가|종목|공시|매수|매도|폭등|폭락',  # Keywords related to stock trading
#         r'vip|vvip',  # Keywords related to exclusive memberships
#         r'전화|문자',  # Keywords related to communication
#         r'축하|건강|생신|생일',  # Keywords related to celebrations or greetings
#         r'서울교통공사|교통카드',  # Keywords related to public transportation
#         r'LH|성남복정',  # Keywords related to real estate or housing
#         r'단독제휴',  # Keywords related to exclusive partnerships
#         r'신청',  # Keywords related to applications or registrations
#         r'기업과',  # Keywords related to business deals or collaborations
#         r'분석|추천|시황',  # Keywords related to stock analysis or recommendations
#         r'금일부터|시작',  # Keywords related to time-sensitive events or promotions
#         r'광고|안내|홍보|이벤트|할인|혜택',  # Keywords related to advertising or promotions
#         r'공짜|무료|증정|선착순',  # Keywords related to freebies or giveaways
#     ]
    
#     # Define a regular expression to match any of the above patterns
#     spam_regex = re.compile('|'.join(regex_list), re.IGNORECASE)
    
#     # Check if the text matches the spam pattern
#     return bool(spam_regex.search(text))

# df = pd.read_csv('spam_data_v0.csv')
# res_spam_normal = f"{df.spam.apply(is_spam).sum()} / {len(df)}, {df.normal.apply(is_spam).sum()}/{len(df)}"
# print(res_spam_normal)
# '''


# print(count_token('spam message examples'))
# print(count_token(TXT))
# print(len(TXT.strip().split())) # factor 5 for korean sms

# print(count_token(CODE))
# print(len(CODE.strip().split())) # factor 5 for korean sms

# print(count_token(EN))
# print(len(EN.strip().split())) # factor 5 for korean sms
