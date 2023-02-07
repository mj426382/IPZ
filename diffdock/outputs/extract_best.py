import numpy as np
import os
from pathlib import Path


def extract_folder(folder_name):
    folder = Path(folder_name)
    target_folder = Path('7nn0_as1')
    for sub in folder.iterdir():
        if sub.is_dir():
            target_file = sub/"rank1.sdf"
            print(sub.name)
            print(target_file.resolve())
            after_move = target_folder/ (str(sub.name)+".sdf")
            target_file.rename(after_move)
#print(os.listdir(folder))
folders = ['batch1_7nn0_as1', 'batch2_7nn0_as1', 'batch3_7nn0_as1']
for f in folders:
    extract_folder(f)
