from pathlib import Path
import subprocess as sb

config_root = Path('config_yamls')
yamls15 = config_root.glob('cold2*15.yaml')
# yamls10 = config_root.glob('cold2*10.yaml')
# yamls3 = config_root.glob('cold2*3.yaml')
# cmds15 = [f'python 1_0_decision_trees_cold.py --config_file {ymlf}' for ymlf in yamls15]
# cmds10 = [f'python 1_0_decision_trees_cold.py --config_file {ymlf}' for ymlf in yamls10]
# cmds3 = [f'python 1_0_decision_trees_cold.py --config_file {ymlf}' for ymlf in yamls3]
# for cmd in cmds10:
#     print(cmd)
#     sb.call(cmd, shell=True)

# for cmd in cmds3:
#     print(cmd)
#     sb.call(cmd, shell=True)

# for cmd in cmds15:
#     print(cmd)
#     sb.call(cmd, shell=True)