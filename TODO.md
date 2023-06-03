

# test: TP=94.4% FP=2.82% (total ~100 examples) / train: TP=90.9% FP=11% (total ~300 examples)
- [x] 프롬프트 찾기
    - 하나의 함수를 만들기. Act as
    - GPT4 성능이 어느정도는 커버쳐준다.
    - GPT3.5: 결과값 파싱이 어렵고 성능이 보장되지 않음, 속도는 2.5배 정도 빠르긴 한데 파싱함수를 오지게 짜야해서 하고 싶지가 않아짐...

- [x] 데이터 파싱
    - [x] 너무 긴 문자: 스팸은 거의 모든 부위가 스팸이다. 그러므로 너무 길다면 조금씩 잘라서 넣자. 물론 멀쩡한 문자도 이러니까 길다 싶으면 잘라서 넣자
        - [x] 긴 문자 분리하기 로직은 삭제. 잘라서 넣기랑 겹치기도 하고 normal 문자 처리가 귀찮다.
    - [x] 토큰 길이 파악: example 하나당 80토큰
    - [x] 긴 정상적인 url과 \[Web발신\] 같은 함정 패턴 데이터에서 제거
    - [x] prepare testset 
    - [x] 데이터셋 추가 업데이트 유도
        - [x] 데이터 새 버전으로 testset 만들기, 그걸로 실험하기


- [ ] 랜덤포레스트 
    - [ ] algorithm
        - [x] coldstart
            - [x] evaluate each function when they get generated: assume functions are perfectly working for seen examples 
            - [x] covering dataset more than once
            - [ ] write file after epoch -> just after gpt inference
        - [ ] warmstart - langchain
            - [ ] cold function -> sample failure cases -> modify function
            - [ ] 걱정스러운 케이스들 (인증번호 등) 을 첨가해서 진행해보자
    - [ ] evaluation
        - [x] innerset recording --> later use for static evals
        - [x] nctx weighting 을 구현해놓긴 함. 근데 아래와 같은 문제가...
            - [x] <code>pd.concat([df]*nctx)</code> 로 해놔서 나중에 터질 우려가 있다.

    - [ ] analyses -> wandb 
        - [x] false positive 예시 모아보기
        - [x] coverage 1, 2, 3, 4... 실험
        - [x] nctx 3 vs 10 vs 15
            - [x] niters, nctxwise...
                - [x] niter=4, nctx=15 의 1번 variation이 잘함, thld 0.35, 0.36 설정 [wandb](https://wandb.ai/sonsus/scamtext/runs/f4w58kcd?workspace=user-sonsus)
                - [x] 그 외 ctx=3, 10 에서도 이 정도 성능 나오는 세팅이 한 개씩 있음
            - [x] nctx 3+10+15 and all niters
        - [x] gpt3.5-turbo vs **gpt4**
        - [x] nctx weighted voting이 더 성능 좋음: nctx 3 (5 coverage) + nctx 10 (7 coverage) 일 때
        - [x] threshold 슬라이딩 하면서 TP와 FP 그래프로 찍어보기 (wandb, 현재는 텍스트로)
        - [ ] fp를 참조하여 chaining?


    - [x] inference
        - [x] parallel execution of multiple functions
            - [x] debugging
            - [ ] profiling
                - 걱정되는 input들 (16개 예시) 에 대해서 진행 (3_inputmsgs.csv) -> multiprocessing / single (25s vs 0.08s ... 잘못된 결과) 
            - [x] packaging to a function (wrapped/)
                - [ ] porting to .kt files

