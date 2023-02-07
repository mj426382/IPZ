# def extract_folder(folder_name):
#     folder = Path(folder_name)
#     target_folder = Path('7nn0_as1')
#     for sub in folder.iterdir():
#         if sub.is_dir():
#             target_file = sub/"rank1.sdf"
#             print(sub.name)
#             print(target_file.resolve())
#             after_move = target_folder/ (str(sub.name)+".sdf")
#             target_file.rename(after_move)
# #print(os.listdir(folder))
# folders = ['batch1_7nn0_as1', 'batch2_7nn0_as1', 'batch3_7nn0_as1']
# for f in folders:
#     extract_folder(f)


from pathlib import Path
import os
from multiprocessing.pool import ThreadPool
import tqdm
import time
import subprocess
import os

def score_conformation_nonminimized(task):
    receptor, input, output = task
    #print(f"{receptor=}, {input=}, {output=}")
    env = dict(os.environ)
    #env["CUDA_VISIBLE_DEVICES"]=""
    with open(output, "w") as outfile:
        subprocess.run(["gnina", "-r", receptor, "-l", input, "--score_only"], stdout=outfile, stderr=subprocess.STDOUT, env=env)

def process_folder(folder_name, receptor_path, n_parallel=4):
    output_folder_name = folder_name + "_output_nonminimized_gpu"
    folder = Path(folder_name)
    output_folder = Path(output_folder_name)
    os.makedirs(output_folder, exist_ok=True)
    tasks = []
    for input in folder.iterdir():
        input_path = input.resolve()
        filename = input_path.name
        output_filename = str(filename) + ".txt"
        output_path = output_folder / output_filename
        input_path_string = str(input_path.resolve())
        output_path_string = str(output_path.resolve())
        receptor_path_string = str(receptor_path.resolve())
        tasks.append((receptor_path_string, input_path_string, output_path_string))

    with ThreadPool(n_parallel) as pool:
        print("in pool")
        iterator = pool.imap_unordered(score_conformation_nonminimized, tasks)
        for _ in tqdm.tqdm(iterator, total=len(tasks)):
            pass
        
    

# folder_name ="6zsl_as1"
# receptor_path = Path("reduce_6zsl_as1.pdb")

folder_name = "7nn0_as1"
receptor_path = Path("reduce_7nn0_as1.pdb")
process_folder(folder_name, receptor_path=receptor_path)