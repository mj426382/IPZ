from rdkit import Chem
import pathlib

NAME_PROPERTY = "_MOLSMILES"

def merge_folder(folder_name, output_sdf):
    mols = []
    to_merge = pathlib.Path(folder_name)
    for input_path in to_merge.iterdir():
        n=0
        input_str = str(input_path.resolve())
        input_name = input_path.name
        input_smiles = input_name.split("____")[-1][:-len(".sdf")]
        suppl = Chem.SDMolSupplier(input_str)
        for mol in suppl:
            mol.SetProp(NAME_PROPERTY, input_smiles)
            mols.append(mol)
            n+=1             
        assert n==1
    
    with Chem.SDWriter(output_sdf) as w:
        for m in mols:
            w.write(m)

merge_folder("6zsl_as1", "6zsl_poses.sdf")
merge_folder("7nn0_as1", "7nn0_poses.sdf")