from omegaconf import OmegaConf
from pathlib import Path 
ctx3 = { 1:    ['gpt-4_nhop0_n_ctx3_0*x',
     'gpt-4_nhop0_n_ctx3_1*x',
     'gpt-4_nhop0_n_ctx3_2*x',
     'gpt-4_nhop0_n_ctx3_3*x',
     'gpt-4_nhop0_n_ctx3_4*x',
     'gpt-4_nhop0_n_ctx3_5*x',],
     2:[
     'gpt-4_nhop0_n_ctx3_[0-1]*x',
     'gpt-4_nhop0_n_ctx3_[4-5]*x',],
     3: [
     'gpt-4_nhop0_n_ctx3_[0-2]*x',
     'gpt-4_nhop0_n_ctx3_[3-5]*x',],
     4: [
     'gpt-4_nhop0_n_ctx3_[0-3]*x',
     'gpt-4_nhop0_n_ctx3_[2-5]*x',],
     5: [
     'gpt-4_nhop0_n_ctx3_[0-4]*x',
     'gpt-4_nhop0_n_ctx3_[1-5]*x',],
     6: [
     'gpt-4_nhop0_n_ctx3_[0-5]*x',]
}


ctx10 = {1: ['gpt-4_nhop0_n_ctx10_0*x',
     'gpt-4_nhop0_n_ctx10_1*x',
     'gpt-4_nhop0_n_ctx10_2*x',
     'gpt-4_nhop0_n_ctx10_3*x',
     'gpt-4_nhop0_n_ctx10_4*x',
     'gpt-4_nhop0_n_ctx10_5*x',
     'gpt-4_nhop0_n_ctx10_6*x',],
 2: ['gpt-4_nhop0_n_ctx10_[0-1]*x',
     'gpt-4_nhop0_n_ctx10_[5-6]*x',],
 3: ['gpt-4_nhop0_n_ctx10_[0-2]*x',
     'gpt-4_nhop0_n_ctx10_[4-6]*x',],
 4: ['gpt-4_nhop0_n_ctx10_[0-3]*x',
     'gpt-4_nhop0_n_ctx10_[3-6]*x',],
 5: ['gpt-4_nhop0_n_ctx10_[0-4]*x',
     'gpt-4_nhop0_n_ctx10_[2-6]*x',],
 6: ['gpt-4_nhop0_n_ctx10_[0-5]*x',
     'gpt-4_nhop0_n_ctx10_[1-6]*x',],
 7: ['gpt-4_nhop0_n_ctx10_[0-6]*x'],
 }



ctx15 = {1: [     'gpt-4_nhop0_n_ctx15_0*x',
     'gpt-4_nhop0_n_ctx15_1*x',
     'gpt-4_nhop0_n_ctx15_2*x',
     'gpt-4_nhop0_n_ctx15_3*x',
     'gpt-4_nhop0_n_ctx15_4*x',],
     2:[
     'gpt-4_nhop0_n_ctx15_[0-1]*x',
     'gpt-4_nhop0_n_ctx15_[3-4]*x',],
     3: [
     'gpt-4_nhop0_n_ctx15_[0-2]*x',
     'gpt-4_nhop0_n_ctx15_[2-4]*x',],
     4: [
     'gpt-4_nhop0_n_ctx15_[0-3]*x',
     'gpt-4_nhop0_n_ctx15_[1-4]*x',],
     5: [
     'gpt-4_nhop0_n_ctx15_[0-4]*x',],
}

template_path = Path('config_yamls/cold_ablations/eval_tmp.yaml')
tmpl = OmegaConf.load(template_path)
ctxs = ['ctx3', 'ctx10', 'ctx15']
for ctx in ctxs:
    newparent = template_path.parent / ctx
    newparent.mkdir(parents=True, exist_ok=True)
    for niter, pttnlist in eval(ctx).items():
        for i, pttn in enumerate(pttnlist):
            tmpl.globpattern = pttn
            newpath = newparent /f"{niter}_{i}.yaml"
            with newpath.open('w') as wf:
                wf.write(OmegaConf.to_yaml(tmpl))
    

