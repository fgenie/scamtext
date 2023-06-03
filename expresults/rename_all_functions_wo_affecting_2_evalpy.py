from pathlib import Path
from fire import Fire
def main(dbg:bool=False):
    cwd=Path()
    functionpys = cwd.glob("**/function_*_*_*.py")
    for p in functionpys:
        print(str(p))
        renamed = p.stem.replace('.','_').replace('-','_') + ".py"
        print('\t', str(renamed))
        if dbg:
            continue
        p.rename(str(p.parent/renamed)) # be careful using this ( p.rename(relative_path) will do what you want. p.rename(just newpath.name) will do `mv path ./newpath.name` instead! )
    
        
        
        

if __name__ == '__main__':
    Fire(main)