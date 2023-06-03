from collections import defaultdict
from pprint import pprint 
import subprocess as sb

D = {
    3: [i for i in range(0, 6)],
    10: [i for i in range(0, 7)],
    15: [i for i in range(0, 5)],
}
PD = defaultdict(list)


for nctx in [3, 10, 15]:
    for iter in D[nctx]:
        post = iter - 0 + 1
        if post != 1:
            pattern_post = f'gpt-4_nhop0_n_ctx{nctx}_[0-{iter}]*x'  # greps iter == 0~iter  
            PD[post].append(pattern_post)
        
        pattern1 = f'gpt-4_nhop0_n_ctx{nctx}_{iter}*x' # greps iter
        PD[1].append(pattern1)
        
        pre = D[nctx][-1] - iter + 1
        if pre != 1:
            pattern_pre = f'gpt-4_nhop0_n_ctx{nctx}_[{iter}-{D[nctx][-1]}]*x'
            PD[pre].append(pattern_pre)
PD = {k:sorted(list(set(v))) for k,v in PD.items()}

fname = "gpatterns.txt"
with open('gpatterns.txt','w') as f:
    pprint(PD, f)


for nctx in [3,10,15]:
    grepping = f"n_ctx{nctx}"
    cmd = f'cat {fname} | grep {grepping} > nctx{nctx}.txt'
    sb.call(cmd, shell=True)

