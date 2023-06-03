import subprocess as sb
from pathlib import Path
from fire import Fire


def main(root = 'config_yamls/cold_ablations',
        evalpy = '2_evaluate_roc.py',
        extended_test = True,
        dbg= False,
        ):
    root = Path(root)
    for p in root.glob('ctx*/*yaml'):
        cmd = f'python {evalpy} --config {str(p)} --load_extended_test {"true" if extended_test else "false"}'
        if not dbg:
            sb.call(cmd, shell=True)
        else:
            print(cmd)
    return 



if __name__ == '__main__':
    Fire(main)